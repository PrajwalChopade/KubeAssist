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

Architecture (block view)

<div style="display:flex;flex-wrap:wrap;gap:12px;">
  <div style="flex:1 1 320px;border:1px solid #e6eef8;background:#f7fbff;padding:14px;border-radius:6px;">
    <strong>Ingestion</strong>
    <p style="margin:6px 0 0">`crawler/`, `ingestion/` — load, normalize, and chunk documents; extract metadata.</p>
  </div>
  <div style="flex:1 1 320px;border:1px solid #e6f7ec;background:#f7fff6;padding:14px;border-radius:6px;">
    <strong>Indexing</strong>
    <p style="margin:6px 0 0">`ingestion/embedder.py` + `vectordb/qdrant_manager.py` — create embeddings and persist to vector DB.</p>
  </div>
  <div style="flex:1 1 320px;border:1px solid #fff4e6;background:#fffbf2;padding:14px;border-radius:6px;">
    <strong>Retrieval</strong>
    <p style="margin:6px 0 0">`retrieval/` — BM25, dense, hybrid search strategies and rerankers for multi-stage selection.</p>
  </div>
  <div style="flex:1 1 320px;border:1px solid #f3e6ff;background:#fbf7ff;padding:14px;border-radius:6px;">
    <strong>Generation</strong>
    <p style="margin:6px 0 0">`llm/` — prompt builders and provider wrappers that compose grounded generation responses.</p>
  </div>
  <div style="flex:1 1 320px;border:1px solid #e6f2ff;background:#f7fdff;padding:14px;border-radius:6px;">
    <strong>Interfaces</strong>
    <p style="margin:6px 0 0">`api/` (FastAPI) and `ui/` (Streamlit) — programmatic and interactive access layers.</p>
  </div>
</div>

Tech stack

<table style="border-collapse:collapse;width:100%;font-family:Helvetica,Arial,sans-serif;margin-top:12px">
  <thead>
    <tr>
      <th style="text-align:left;padding:10px;background:#2b7cff;color:#fff;border:1px solid #dfefff">Component</th>
      <th style="text-align:left;padding:10px;background:#2b7cff;color:#fff;border:1px solid #dfefff">Technology</th>
      <th style="text-align:left;padding:10px;background:#2b7cff;color:#fff;border:1px solid #dfefff">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:10px;border:1px solid #eee">Language</td>
      <td style="padding:10px;border:1px solid #eee">Python 3.10+</td>
      <td style="padding:10px;border:1px solid #eee">Main implementation language</td>
    </tr>
    <tr>
      <td style="padding:10px;border:1px solid #eee">API</td>
      <td style="padding:10px;border:1px solid #eee">FastAPI + Uvicorn</td>
      <td style="padding:10px;border:1px solid #eee">ASGI server for programmatic access</td>
    </tr>
    <tr>
      <td style="padding:10px;border:1px solid #eee">UI</td>
      <td style="padding:10px;border:1px solid #eee">Streamlit</td>
      <td style="padding:10px;border:1px solid #eee">Lightweight interactive demo app</td>
    </tr>
    <tr>
      <td style="padding:10px;border:1px solid #eee">Vector DB</td>
      <td style="padding:10px;border:1px solid #eee">Qdrant (pluggable)</td>
      <td style="padding:10px;border:1px solid #eee">ANN store for embeddings; design is pluggable</td>
    </tr>
    <tr>
      <td style="padding:10px;border:1px solid #eee">Retrieval</td>
      <td style="padding:10px;border:1px solid #eee">BM25, dense, hybrid</td>
      <td style="padding:10px;border:1px solid #eee">Multiple strategies supported</td>
    </tr>
    <tr>
      <td style="padding:10px;border:1px solid #eee">Embeddings</td>
      <td style="padding:10px;border:1px solid #eee">Provider-agnostic</td>
      <td style="padding:10px;border:1px solid #eee">Swap models/providers as needed</td>
    </tr>
    <tr>
      <td style="padding:10px;border:1px solid #eee">Testing & tooling</td>
      <td style="padding:10px;border:1px solid #eee">pytest, black, ruff, Docker</td>
      <td style="padding:10px;border:1px solid #eee">Standard Python tooling</td>
    </tr>
  </tbody>
</table>

Tradeoffs (highlights)

<div style="margin-top:12px;display:flex;flex-direction:column;gap:10px">
  <div style="border-left:4px solid #ff9900;background:#fff8ec;padding:12px;border-radius:4px;">
    <strong>Retrieval vs. Generation</strong>
    <p style="margin:6px 0 0">RAG gives grounded answers but requires a complete index and careful retrieval tuning. Pure generation is simpler but risks hallucination. This repo prioritizes retrieval-first patterns to favor source grounding.</p>
  </div>
  <div style="border-left:4px solid #2b7cff;background:#eef7ff;padding:12px;border-radius:4px;">
    <strong>Vector DB choice</strong>
    <p style="margin:6px 0 0">Qdrant is chosen for local development and reproducibility. Managed offerings (for example Pinecone or Weaviate) reduce operational burden and scale better, at cost.</p>
  </div>
  <div style="border-left:4px solid #7bd389;background:#f5fff6;padding:12px;border-radius:4px;">
    <strong>Embeddings: quality vs. cost</strong>
    <p style="margin:6px 0 0">Better models improve retrieval at increased cost and latency. The embedding layer is provider-agnostic so teams can select models matching budget and SLA goals.</p>
  </div>
</div>

Notes

- Keep large generated data out of commits. Use `data/` and `qdrant_data/` for local artifacts only (these paths are included in the project's `.gitignore`).
- Configure LLM and vector DB credentials using environment variables; refer to `llm/` and `vectordb/` for client utilities.

Contributing

- Please open an issue before submitting substantial changes.
- Include tests for new features and follow the repo style.

License & contact

- This repo currently has no explicit license file. Add a `LICENSE` to make licensing clear.
- For questions or feature requests, open an issue in this repository.
