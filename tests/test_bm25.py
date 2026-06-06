from retrieval.bm25 import bm25_search

results = bm25_search(
    "deployment rollout"
)

for r in results:

    print("=" * 100)

    print(r["text"][:500])