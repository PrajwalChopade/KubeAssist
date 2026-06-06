from retrieval.hybrid import hybrid_search
from retrieval.reranker import rerank

query = "deployment rollout"

docs = hybrid_search(
    query,
    top_k=20
)

reranked = rerank(
    query,
    docs,
    top_k=5
)

for doc in reranked:

    print("=" * 100)

    if hasattr(doc, "payload"):
        print(doc.payload["text"][:1000])
    else:
        print(doc["text"][:1000])