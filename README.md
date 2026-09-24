# 🏥 Medical Chatbot (RAG-Powered)

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-red.svg)](https://flask.palletsprojects.com/)
[![Orchestration](https://img.shields.io/badge/Orchestration-LangChain-green.svg)](https://python.langchain.com/)
[![Vector Store](https://img.shields.io/badge/Vector%20Store-FAISS-purple.svg)](https://github.com/facebookresearch/faiss)
[![LLM Acceleration](https://img.shields.io/badge/Inference-Groq%20Cloud-orange.svg)](https://groq.com/)

A production-grade, domain-specific Medical Q&A Chatbot built using **Retrieval-Augmented Generation (RAG)**. The application indexes authoritative medical reference literature, creates dense semantic embeddings, and uses high-speed Groq-accelerated LLMs to deliver accurate, context-grounded medical insights via an intuitive web interface with persistent chat history.

---

## 📌 Architecture Overview

```
                          ┌───────────────────────────┐
                          │ Medical Literature (PDFs) │
                          └─────────────┬─────────────┘
                                        │
                                        ▼ (PyPDFLoader)
                          ┌───────────────────────────┐
                          │   Document Chunking       │
                          │ (RecursiveCharacterSplit) │
                          └─────────────┬─────────────┘
                                        │
                                        ▼ (HuggingFace all-MiniLM-L6-v2)
                          ┌───────────────────────────┐
                          │   Dense Vector Store      │
                          │       (FAISS DB)          │
                          └─────────────┬─────────────┘
                                        │
User Query ──► [ Flask Web App ]        │
                     │                  ▼
                     ├──► [ Semantic Retriever ] ──► Extracts Top-K Relevant Context
                     │                                         │
                     └──► [ Medical Prompt + Context ] ────────┘
                                        │
                                        ▼
                             [ Groq LLM Inference ]
                                        │
                                        ▼
                       [ Verified Answer + SQLite History ]
```

---

## ✨ Features

- **Document Ingestion & Chunking**: Automatically processes reference medical encyclopedias and documents using `PyPDFLoader` and `RecursiveCharacterTextSplitter` configured for optimal chunk size (`550`) and overlap (`60`).
- **Dense Vector Search**: Generates 384-dimensional embeddings via `sentence-transformers/all-MiniLM-L6-v2` and persists them in a high-performance **FAISS** vector index.
- **Ultra-Fast Inference**: Integrates with **Groq Cloud API** for rapid response generation with minimal latency.
- **Context-Bound Guardrails**: Employs medical prompt engineering instructing the LLM to formulate clear, concise answers strictly based on retrieved context.
- **Persistent Chat History**: Built-in **SQLite** database stores all conversations with timestamps, individual message deletion, and complete chat clearing.
- **Robust Error Handling & Logging**: Enterprise-grade custom exception hierarchy (`CustomException`) and rotating time-stamped execution logs.
- **Responsive Web UI**: Clean, accessible web interface built on Flask and Jinja2 templates.

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| **Language** | Python 3.10+ |
| **Web Framework** | Flask |
| **LLM Orchestration** | LangChain / LangChain-Community / LangChain-Groq |
| **Embeddings** | Hugging Face (`sentence-transformers/all-MiniLM-L6-v2`) |
| **Vector Database** | Facebook AI Similarity Search (FAISS) |
| **LLM Provider** | Groq (`openai/gpt-oss-120b` or custom configured model) |
| **Storage / DB** | SQLite3 (`chat_history.db`) |
| **PDF Processing** | PyPDF |

---

## 📁 Repository Structure

```text
├── app/
│   ├── common/                  # Shared utilities
│   │   ├── custom_exceptions.py # Custom application exception handlers
│   │   └── logger.py            # Centralized logging setup
│   ├── componenets/             # Core RAG pipeline modules
│   │   ├── embeddings.py        # HuggingFace embeddings loader
│   │   ├── history.py           # SQLite conversation history manager
│   │   ├── load_llm.py          # Groq LLM client initializer
│   │   ├── main.py              # Data ingestion pipeline entry point
│   │   ├── pdf_load.py          # PDF document reader & text splitter
│   │   ├── retriver.py          # Custom prompt & RetrievalQA chain builder
│   │   └── vector_store.py      # FAISS vector store creation & loading
│   ├── config/
│   │   └── config.py            # Global paths, chunk sizes, and API configurations
│   ├── templates/
│   │   └── index.html           # Front-end chatbot interface
│   └── application.py           # Flask server routes & application entry point
├── data/                        # Medical reference datasets & literature (PDFs)
├── vector_db/                   # Serialized FAISS index files
├── running_d/                   # Automated runtime execution logs
├── req.txt                      # Project dependencies
├── setup.py                     # Package setup script
└── README.md                    # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.10 or higher
- Git
- A free **Groq API Key** from [console.groq.com](https://console.groq.com/)

### 2. Clone the Repository

```bash
git clone https://github.com/smk187691-sys/-medical_chatbot-RAG-.git
cd -medical_chatbot-RAG-
```

### 3. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r req.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory and supply your Groq API credentials:

```env
GROQ_API_KEY=gsk_your_groq_api_key_here
```

---

## 📖 Usage

### Step 1: Ingest Data & Build Vector Database (Optional if pre-indexed)

If you add new medical reference PDFs into `data/`, run the ingestion script to process the documents and create the FAISS index:

```bash
python -m app.componenets.main
```

### Step 2: Run the Web Application

Launch the Flask application:

```bash
python -m app.application
```

Open your browser and navigate to:
```
http://localhost:5000
```

---

## 💬 Application Endpoints

| Route | Method | Description |
|---|---|---|
| `/` | `GET` | Renders chatbot UI with existing message history |
| `/` | `POST` | Submits user medical query, invokes RAG chain, and returns response |
| `/delete/chat/<chat_id>` | `GET` | Deletes a specific conversation thread by ID |
| `/clear` | `GET` | Clears all stored chat history |

---

## ⚠️ Medical Disclaimer

> **IMPORTANT**: This chatbot is intended solely for educational and informational purposes as a technical demonstration of Retrieval-Augmented Generation (RAG). It is **not** a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider with any medical questions.

---

## 👨‍💻 Author

- **Mohit Kumar** ([@smk187691-sys](https://github.com/smk187691-sys))
