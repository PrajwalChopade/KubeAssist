<p align="center">

# 🚀 Kube-Assist

### Kubernetes Support Assistant powered by Retrieval-Augmented Generation (RAG)

Semantic search, hybrid retrieval, and LLM-powered responses over Kubernetes documentation and operational knowledge.

<p>

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Qdrant](https://img.shields.io/badge/Qdrant-Vector%20Database-red)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![RAG](https://img.shields.io/badge/Architecture-RAG-purple)

</p>

</p>

---

## Overview

Kube-Assist is a production-oriented Retrieval-Augmented Generation (RAG) system designed to provide accurate, source-grounded answers for Kubernetes-related queries.

The platform ingests Kubernetes documentation, configuration guides, troubleshooting references, and operational knowledge, transforms them into searchable vector representations, and retrieves relevant context to generate reliable responses using Large Language Models.

---

## Key Features

* Document ingestion and preprocessing
* Semantic chunking and metadata extraction
* Embedding generation and vector indexing
* Qdrant-powered vector search
* BM25, Dense, and Hybrid Retrieval
* Context-aware answer generation
* FastAPI backend services
* Streamlit web interface
* Dockerized deployment
* RAGAS evaluation framework

---

## Architecture

```text
                    ┌─────────────────┐
                    │  Kubernetes     │
                    │ Documentation   │
                    └────────┬────────┘
                             │
                             ▼
                 ┌─────────────────────┐
                 │ Ingestion Pipeline  │
                 └────────┬────────────┘
                          │
                          ▼
                 ┌─────────────────────┐
                 │ Text Chunking       │
                 │ Metadata Extraction │
                 └────────┬────────────┘
                          │
                          ▼
                 ┌─────────────────────┐
                 │ Embedding Model     │
                 └────────┬────────────┘
                          │
                          ▼
                 ┌─────────────────────┐
                 │ Qdrant Vector Store │
                 └────────┬────────────┘
                          │
            ┌─────────────┴─────────────┐
            ▼                           ▼
      Dense Retrieval           BM25 Retrieval
            │                           │
            └───────────┬───────────────┘
                        ▼
                Hybrid Retrieval
                        │
                        ▼
                   Reranking
                        │
                        ▼
                 Context Builder
                        │
                        ▼
                      LLM
                        │
                        ▼
                Generated Answer
```

---

## Technology Stack

| Layer            | Technology                        |
| ---------------- | --------------------------------- |
| Language         | Python 3.10+                      |
| Backend          | FastAPI                           |
| UI               | Streamlit                         |
| Vector Database  | Qdrant                            |
| Retrieval        | BM25, Dense Search, Hybrid Search |
| Embeddings       | Sentence Transformers             |
| LLM Integration  | OpenAI / Local Models             |
| Evaluation       | RAGAS                             |
| Containerization | Docker                            |

---

## Repository Structure

```bash
kube-assist/
│
├── api/
│   └── FastAPI services
│
├── crawler/
│   └── Documentation crawling
│
├── ingestion/
│   ├── loader.py
│   ├── chunker.py
│   └── embedder.py
│
├── retrieval/
│   ├── dense.py
│   ├── bm25.py
│   ├── hybrid.py
│   └── reranker.py
│
├── vectordb/
│   └── qdrant_manager.py
│
├── llm/
│   └── LLM integrations
│
├── ui/
│   └── Streamlit application
│
├── evaluation/
│   └── ragas_eval.py
│
├── data/
│
├── docker-compose.yml
│
└── README.md
```

---

## Getting Started

### Clone Repository

```bash
git clone https://github.com/<username>/kube-assist.git

cd kube-assist
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Start Qdrant

```bash
docker compose up -d
```

### Run API Server

```bash
uvicorn api.main:app --reload
```

### Launch UI

```bash
streamlit run ui/app.py
```

---

## Retrieval Pipeline

| Stage      | Description                            |
| ---------- | -------------------------------------- |
| Ingestion  | Load and preprocess documentation      |
| Chunking   | Split documents into retrievable units |
| Embedding  | Generate vector representations        |
| Indexing   | Store vectors in Qdrant                |
| Retrieval  | Dense, BM25, or Hybrid Search          |
| Reranking  | Improve relevance ordering             |
| Generation | Produce grounded responses             |

---

## Evaluation

The system is evaluated using RAGAS across:

* Faithfulness
* Context Precision
* Context Recall
* Answer Relevancy

Run evaluation:

```bash
python -m evaluation.ragas_eval
```

---

## Example Query

**Question**

```text
How does Kubernetes schedule Pods onto Nodes?
```

**Response**

```text
Kubernetes uses the Scheduler component to assign Pods
to Nodes based on resource requirements, constraints,
taints, tolerations, and scheduling policies.
```

---

## Future Enhancements

* Multi-query retrieval
* Query expansion
* Cross-encoder reranking
* Semantic caching
* Observability and monitoring
* Kubernetes deployment
* CI/CD automation

---


