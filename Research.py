import os
import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import Ollama


# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🧠",
    layout="wide"
)

# -----------------------------
# Custom Styling
# -----------------------------

st.markdown(
    """
    <style>
    .main-title {
        text-align:center;
        font-size:40px;
        font-weight:bold;
        color:#4CAF50;
    }

    .subtitle {
        text-align:center;
        font-size:18px;
        color:gray;
        margin-bottom:30px;
    }

    .stChatMessage {
        border-radius:10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Title Section
# -----------------------------

st.markdown('<p class="main-title">🧠 AI Research Assistant</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Ask questions from research papers using RAG + Local LLM</p>',
    unsafe_allow_html=True
)

# -----------------------------
# Directories
# -----------------------------

DATA_DIR = "documents"
DB_DIR = "vectorstore"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(DB_DIR, exist_ok=True)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("⚙️ Controls")

st.sidebar.markdown("### 📄 Upload Research Papers")

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    file_path = os.path.join(DATA_DIR, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.sidebar.success("✅ File uploaded successfully!")

st.sidebar.markdown("---")

st.sidebar.markdown("### 🤖 Model")

model_name = st.sidebar.selectbox(
    "Choose Ollama Model",
    ["mistral", "llama3"]
)

# -----------------------------
# Vector Database Creation
# -----------------------------

@st.cache_resource
def create_vector_store():

    docs = []

    for file in os.listdir(DATA_DIR):

        if file.endswith(".pdf"):

            loader = PyPDFLoader(os.path.join(DATA_DIR, file))
            docs.extend(loader.load())

    if len(docs) == 0:
        return None

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR
    )

    return vectordb


# -----------------------------
# QA Chain
# -----------------------------

@st.cache_resource
def load_chain(model):

    vectordb = create_vector_store()

    if vectordb is None:
        return None

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    llm = Ollama(model=model)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    return qa_chain


# -----------------------------
# Chat Memory
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Chat History
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User Input
# -----------------------------

prompt = st.chat_input("Ask a question about your research papers...")

qa_chain = load_chain(model_name)

if prompt:

    if qa_chain is None:
        st.warning("⚠️ Please upload a research paper first.")
    else:

        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("🔍 Searching documents..."):

                response = qa_chain.run(prompt)

            st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )
