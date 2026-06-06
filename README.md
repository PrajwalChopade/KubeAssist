<p align="center">
  <img alt="kube-assist" src="https://img.shields.io/badge/kube--assist-Documentation-blueviolet" />
  <img alt="python" src="https://img.shields.io/badge/Python-3.10%2B-blue" />
  <img alt="qdrant" src="https://img.shields.io/badge/VectorDB-Qdrant-green" />
  <img alt="license" src="https://img.shields.io/badge/License-Add%20LICENSE-lightgrey" />
</p>

# kube-assist

kube-assist is a focused Retrieval-Augmented Generation (RAG) assistant for Kubernetes support and documentation retrieval. It combines ingestion, vector search, and LLM-based generation to provide source-grounded answers and configuration assistance.

This repository includes components for crawling and parsing cluster/config docs, chunking and embedding text, indexing into a vector store, retrieval and reranking strategies, an API layer, and a Streamlit UI for demos.

Why this project

- Faster, context-aware help for Kubernetes operators and engineers.
- Reproducible ingestion and indexing pipeline for documentation.
- Extensible retrieval and LLM integration.

Table of contents

- [Quick start](#quick-start)
- [Features](#features)
- [Architecture](#architecture)
- [Tech stack](#tech-stack)
- [Tradeoffs & design considerations](#tradeoffs--design-considerations)
- [Development & testing](#development--testing)
- [Contributing](#contributing)
- [License & contact](#license--contact)

Quick start

Prerequisites

- Python 3.10+ (virtual environment recommended)
- Docker & docker-compose (optional — used for Qdrant or local services)

Install

```bash
python -m venv venv
venv\\Scripts\\activate    # Windows
pip install -r requirements.txt
```

Run (development)

```bash
# Start API
uvicorn api.main:app --reload

# Start interactive UI
streamlit run ui/app.py

# Or run services via Docker Compose
docker-compose up --build
```

Notes

- Qdrant: If using vector DB, ensure the service is available and update `vectordb/qdrant_manager.py` if needed.
- LLM keys: Configure provider credentials as environment variables; see `llm/` for client wrappers.

Features

- Ingestion pipeline: document parsing, chunking and metadata extraction.
- Embedding & indexing: provider-agnostic embedding layer and Qdrant integration.
- Flexible retrieval: BM25, dense, and hybrid search strategies with reranking.
- LLM-backed generation: source-grounded answers with prompt-building utilities.
- API + UI: programmatic endpoints and a Streamlit demo for quick testing.

Architecture

The system is organized into clear layers:

- Ingestion: `crawler/`, `ingestion/` — load and prepare text, chunk documents.
- Indexing: `ingestion/embedder.py` + `vectordb/qdrant_manager.py` — create and persist embeddings.
- Retrieval: `retrieval/` — search strategies (BM25, dense, hybrid) and rerankers.
- Generation: `llm/` — prompt builders and LLM client wrappers.
- Interfaces: `api/` (FastAPI) and `ui/` (Streamlit) for users and integrations.

Tech stack

- Language: Python 3.10+
- API: FastAPI + Uvicorn
- UI: Streamlit
- Vector DB: Qdrant (pluggable)
- Retrieval techniques: BM25, dense embeddings, hybrid approaches
- Embeddings: provider-agnostic (configurable)
- Testing: pytest
- Dev tools: Docker / docker-compose, formatters (black), linters (ruff)

Tradeoffs & design considerations

- Retrieval vs. Generation
  - RAG yields grounded answers but needs good index coverage and retrieval tuning. Pure generation is simpler but risks hallucination. The repo uses retrieval-first patterns to prioritize source grounding.

- Vector DB (Qdrant) vs. managed services
  - Qdrant is great for local dev and reproducibility. Managed services (Pinecone, Weaviate) reduce ops overhead and scale better but cost more.

- Embedding model quality vs. cost & latency
  - Higher-quality embeddings improve recall and ranking at increased cost. The system is model-agnostic so operators can choose a tradeoff appropriate to budget and SLAs.

- Freshness vs. indexing complexity
  - Real-time indexing requires watchers and more infra; batch indexing is cheaper but introduces staleness. The repo provides change detection primitives to make updates incremental.

- Hybrid retrieval complexity
  - Combining BM25 and dense retrieval improves results but increases tuning surface; hybrid is optional with simple fallbacks.

- Privacy
  - Ingested content may include secrets. Sanitize or redact sensitive data before ingestion and store credentials in environment variables or secret managers.


Development & testing

Run tests

```bash
pytest -q
```

Lint & format

```bash
black .
ruff check .
```

Notes

- Keep large generated data out of commits. Use `data/` and `qdrant_data/` for local artifacts only.

Configuration & environment variables

- Check `requirements.txt` for runtime dependencies.
- Typical environment variables to set (examples — review code for exact variable names):
  - `OPENROUTER_API_KEY` or other LLM provider key
  - `QDRANT_URL` / `QDRANT_API_KEY` when using remote Qdrant
  - Any provider-specific model or endpoint configuration under `llm/`

Testing and evaluation

- Unit tests are in `tests/`. CI should run `pytest` and optionally build a small qdrant instance in Docker for integration tests.
- Evaluation utilities and scripts are under `evaluation/` (e.g., `ragas_eval.py`, `build_eval_data.py`). Use these to measure retrieval and generation quality.

Extending the system

- To add a new document source: implement a crawler in `crawler/` and add a parser in `crawler/parser.py`.
- To add a new retriever or reranker: add modules under `retrieval/` and wire them into the query flow in `rag/query_engine.py`.
- To swap LLM backends: update or extend `llm/openrouter_client.py` and `llm/generate.py` to support provider-specific SDKs.

Security & privacy

- Treat any uploaded or ingested documents as potentially sensitive. Sanitize or redact secrets before ingestion.
- Do not commit API keys or secrets into the repository. Use environment variables or secret managers.

Maintenance & troubleshooting

- If embeddings fail or are inconsistent, re-run chunking and embedding for the affected dataset.
- For Qdrant connectivity issues, verify the host/port and API keys, and consult `vectordb/qdrant_manager.py` for default behavior.


Contributing

- Please open an issue before submitting substantial changes.
- Include tests for new features and follow the repo style.

License & contact

- This repo currently has no explicit license file. Add a `LICENSE` to make licensing clear.
- For questions or feature requests, open an issue in this repository.
