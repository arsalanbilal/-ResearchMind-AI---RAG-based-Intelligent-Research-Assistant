import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain.chains import RetrievalQA

DB_PATH = "vectorstore"

# Page config
st.set_page_config(
    page_title="ResearchMind AI",
    page_icon="🔬",
    layout="wide"
)

# Header
st.title("🔬 ResearchMind AI")
st.markdown("### Your Intelligent Research Assistant")

st.markdown("---")

# Sidebar
st.sidebar.title("⚙️ Settings")

model_name = st.sidebar.selectbox(
    "Choose LLM Model",
    ["llama3"]
)

temperature = st.sidebar.slider(
    "Creativity Level",
    0.0,
    1.0,
    0.3
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Upload research papers in the data folder and run ingest.py to index them."
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat interface
st.subheader("💬 Ask Questions About Research Papers")

query = st.chat_input("Ask your research question...")

if query:

    st.session_state.messages.append({"role": "user", "content": query})

    embeddings = OllamaEmbeddings(model=model_name)

    vectorstore = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever()

    llm = ChatOllama(
        model=model_name,
        temperature=temperature
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    answer = qa_chain.run(query)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

# Display chat messages
for message in st.session_state.messages:

    if message["role"] == "user":
        st.chat_message("user").write(message["content"])

    else:
        st.chat_message("assistant").write(message["content"])

st.markdown("---")

# Extra research tools
st.subheader("🧠 Research Tools")

col1, col2 = st.columns(2)

with col1:
    if st.button("📄 Generate Paper Summary"):

        prompt = "Give a concise summary of the research papers."

        embeddings = OllamaEmbeddings(model=model_name)

        vectorstore = Chroma(
            persist_directory=DB_PATH,
            embedding_function=embeddings
        )

        retriever = vectorstore.as_retriever()

        llm = ChatOllama(model=model_name)

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever
        )

        summary = qa_chain.run(prompt)

        st.success(summary)

with col2:
    if st.button("🔑 Extract Key Insights"):

        prompt = "Extract key insights from the research papers."

        embeddings = OllamaEmbeddings(model=model_name)

        vectorstore = Chroma(
            persist_directory=DB_PATH,
            embedding_function=embeddings
        )

        retriever = vectorstore.as_retriever()

        llm = ChatOllama(model=model_name)

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever
        )

        insights = qa_chain.run(prompt)

        st.success(insights)
