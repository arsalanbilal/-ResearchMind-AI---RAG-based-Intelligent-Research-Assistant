# 🧠 AI Research Assistant (RAG Powered)

An **AI-powered research assistant** that can read research papers or company documents and answer questions from them using **Retrieval Augmented Generation (RAG)**.

This project demonstrates how **Large Language Models (LLMs)** can be combined with **vector databases and document retrieval** to build intelligent assistants.

The application allows users to:

* Upload research papers (PDF)
* Ask questions about the documents
* Retrieve relevant information using semantic search
* Generate accurate answers using a local LLM

The interface is built with **Streamlit**, making the application simple and interactive.

---

# 🚀 Features

* 📄 Upload research papers (PDF)
* 🔎 Ask questions about the document
* 🧠 Semantic search using vector embeddings
* 🤖 Local LLM responses using Ollama
* ⚡ Retrieval Augmented Generation (RAG)
* 💬 Chat-style interface
* 🌐 Simple and interactive Streamlit UI

---

# 🏗️ Tech Stack

| Technology            | Purpose                                 |
| --------------------- | --------------------------------------- |
| Python                | Core programming language               |
| LangChain             | LLM orchestration and RAG pipeline      |
| ChromaDB              | Vector database for document embeddings |
| Ollama                | Running LLM locally                     |
| Sentence Transformers | Text embedding model                    |
| Streamlit             | Web application interface               |

---

# 📂 Project Structure

```
AI-Research-Assistant
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation Guide

Follow these steps to run the project locally.

---

# 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI-Research-Assistant.git
cd AI-Research-Assistant
```

---

# 2️⃣ Install Python Dependencies

Make sure you have **Python 3.9 or above** installed.

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

# 3️⃣ Install Ollama

Ollama is used to run **local Large Language Models (LLMs)**.

Download Ollama from the official website:

https://ollama.com/download

After installation, verify it:

```bash
ollama --version
```

---

# 4️⃣ Pull a Model

Download a model that will generate answers.

Example (Mistral model):

```bash
ollama pull mistral
```

You can also use:

```bash
ollama pull llama3
```

---

# 5️⃣ Run Ollama

Start the Ollama server:

```bash
ollama run mistral
```

This will load the model locally.

Keep the terminal running.

---

# 6️⃣ Run the Application

In another terminal, start the Streamlit application:

```bash
streamlit run app.py
```

---

# 7️⃣ Open the Application

After running the command, the app will open in your browser:

```
http://localhost:8501
```

---

# 🧠 How the System Works

The system uses **Retrieval Augmented Generation (RAG)**.

Step-by-step workflow:

1. User uploads research papers.
2. The document is split into smaller text chunks.
3. Each chunk is converted into vector embeddings.
4. Embeddings are stored in a **ChromaDB vector database**.
5. When a user asks a question:

   * The system retrieves the most relevant document chunks.
6. The retrieved context is sent to the **Ollama LLM**.
7. The LLM generates a context-aware answer.

---

# 📊 Architecture

```
User Question
      │
      ▼
Streamlit Interface
      │
      ▼
LangChain RAG Pipeline
      │
      ▼
ChromaDB Vector Search
      │
      ▼
Retrieve Relevant Document Chunks
      │
      ▼
Ollama LLM (Mistral / Llama3)
      │
      ▼
Generated Answer
```

---

# 🎯 Use Cases

* Research paper analysis
* Document question answering
* Knowledge assistants
* Enterprise document search systems
* Academic research assistance

---

# 📌 Future Improvements

Possible enhancements for this project:

* PDF preview inside the app
* Source citations in answers
* Multi-document search
* Research paper summarization
* ArXiv research paper integration
* Conversation memory

---

# 👨‍💻 Author

**Arsalan Bilal**

Aspiring **Data Scientist / Generative AI Engineer** with interest in:

* Generative AI
* Natural Language Processing
* Large Language Models
* Machine Learning Systems

---

# ⭐ If you like this project

Consider giving it a **star on GitHub** ⭐
