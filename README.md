# 🤖 Agentic DocExtract RAG

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-red.svg)](https://docs.pydantic.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An enterprise-grade document processing and Retrieval-Augmented Generation (RAG) system built with **Python**, **FastAPI**, and **AI Agentic Workflows**. 

This system ingests unstructured PDF documents (invoices, contracts, financial reports), extracts structured metadata into a relational database, and indexes semantic embeddings into a vector store to power an intelligent Q&A agent with source citations.

---

## 🏗️ Architecture Overview

```text
 [ Client / User ]
        │
        ▼
 ┌─────────────────────────────────────────────────────────┐
 │                  FastAPI REST Endpoints                 │
 └───────────┬─────────────────────────────────┬───────────┘
             │                                 │
             ▼                                 ▼
   ┌───────────────────┐             ┌───────────────────┐
   │  PDF Extractor    │             │   Chunker & RAG   │
   └─────────┬─────────┘             └─────────┬─────────┘
             │                                 │
             ▼                                 ▼
┌─────────────────────────┐       ┌─────────────────────────┐
│  Relational Database    │       │  Vector Store           │
│  (PostgreSQL)           │       │  (ChromaDB)             │
│  -> Document Metadata   │       │  -> Text Embeddings     │
└─────────────────────────┘       └────────────┬────────────┘
                                               │
                                               ▼
                                  ┌─────────────────────────┐
                                  │   Agentic QA (LLM)      │
                                  └─────────────────────────┘
```

### ✨ Key Features  
* RESTful API Pipeline: Powered by FastAPI for asynchronous file ingestion, validation, and status tracking.
* Structured Data Extraction: Parses unstructured PDFs into type-safe Pydantic schemas.
* Semantic Vector Search: Generates text embeddings and indexes document chunks in ChromaDB for high-accuracy context retrieval.
* Agentic Q&A: Leverages LLMs to answer natural language queries based exclusively on ingested document context with page/source citations.
* Relational Data Persistence: Tracks document ingestion history and metadata via PostgreSQL.
* Production Readiness: Containerized via Docker Compose with automated CI/CD workflows using GitHub Actions.

### 🛠️ Tech Stack
* Language & API: Python 3.11+, FastAPI, Uvicorn, Pydantic v2
* Data Processing: PyPDF / pdfplumber, Pandas
* AI & RAG Engine: LangChain / LlamaIndex, ChromaDB (Vector DB), OpenAI / Claude / GenAI APIs
* Database & ORM: PostgreSQL, SQLAlchemy / SQLModel
* DevOps & Testing: Docker, Docker Compose, Pytest, GitHub Actions (CI/CD)

### 🚀 Getting Started
#### Prerequisites
* Python 3.11 or higher
* Git

#### Local Setup & Installation
1. **Clone the repository**:
```bash
git clone [https://github.com/Santiago22-py/agentic-docextract-rag.git](https://github.com/Santiago22-py/agentic-docextract-rag.git)
cd agentic-docextract-rag
```

2. **Create and activate a virtual environment**:
```bash
python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```
3. **Install dependencies**: 
```bash
pip install -r requirements.txt
```
4. **Environment Variables Configuration**:
```bash
cp .env.example .env
```
5. **Run the FastAPI Dev server**: 
```bash
uvicorn src.main:app --reload
```
6. **Verify the APII**:
```bash
curl -X GET "[http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)"
```

### 🧪 Running Tests
Execute unit and integration tests using ```pytest```:
```bash
pytest -v
```

### 📜 License
Distributed under the MIT License. See ```LICENSE``` for more information.
