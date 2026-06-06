from rank_bm25 import BM25Okapi
import json
from pathlib import Path

CHUNK_DIR = Path("data/chunks")

documents = []
metadata = []

for file in CHUNK_DIR.glob("*.json"):

    with open(file, encoding="utf-8") as f:
        chunk = json.load(f)

    text = chunk["text"]

    documents.append(text.split())
    metadata.append(chunk)

bm25 = BM25Okapi(documents)


def bm25_search(query, top_k=5):

    scores = bm25.get_scores(query.split())

    ranked_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )

    return [
        metadata[i]
        for i in ranked_indices[:top_k]
    ]