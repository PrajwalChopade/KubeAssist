from retrieval.dense import dense_search
from retrieval.bm25 import bm25_search

RRF_K = 60


def hybrid_search(query, top_k=10):

    dense_results = dense_search(
        query,
        top_k=20
    )

    bm25_results = bm25_search(
        query,
        top_k=20
    )

    scores = {}

    documents = {}

    # Dense results
    for rank, doc in enumerate(dense_results):

        chunk_id = doc.payload["chunk_id"]

        documents[chunk_id] = doc

        scores[chunk_id] = (
            scores.get(chunk_id, 0)
            + 1 / (RRF_K + rank + 1)
        )

    # BM25 results
    for rank, doc in enumerate(bm25_results):

        chunk_id = doc["chunk_id"]

        documents[chunk_id] = doc

        scores[chunk_id] = (
            scores.get(chunk_id, 0)
            + 1 / (RRF_K + rank + 1)
        )

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        documents[chunk_id]
        for chunk_id, _ in ranked[:top_k]
    ]