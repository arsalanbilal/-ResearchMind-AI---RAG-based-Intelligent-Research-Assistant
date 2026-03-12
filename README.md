# 🔬 ResearchMind AI – Intelligent Research Assistant

ResearchMind AI is an AI-powered research assistant that allows users to interact with research papers using natural language.  
It uses a Retrieval-Augmented Generation (RAG) pipeline to retrieve relevant information from research documents and generate accurate answers using a local LLM.

The application enables users to upload research papers, ask questions, extract insights, and generate summaries.

---

## 🚀 Features

- Chat with research papers
- AI-generated answers from documents
- Semantic search using vector embeddings
- Research paper summary generation
- Key insights extraction
- Clean and interactive UI
- Local LLM support using Ollama

---

## 🧠 Tech Stack

- Python
- LangChain
- ChromaDB
- Ollama LLM
- Streamlit

Libraries used:

- langchain
- chromadb
- streamlit
- langchain-ollama
- pypdf
- sentence-transformers

---

# Project Architecture:
Research Papers
       ↓
Document Loader
       ↓
Text Chunking
       ↓
Embeddings
       ↓
Vector Database (ChromaDB)
       ↓
Retriever
       ↓
Ollama LLM
       ↓
AI Generated Answer


## 📂 Project Structure

ai-research-assistant
│
├── app.py
├── ingest.py
├── requirements.txt
│
├── data
│ └── research_papers
│
├── vectorstore
│
└── README.md
