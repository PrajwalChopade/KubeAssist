from retrieval.hybrid import hybrid_search

results = hybrid_search(
    "deployment rollout"
)

for r in results:

    print("=" * 100)

    if hasattr(r, "payload"):
        print(r.payload["text"][:500])

    else:
        print(r["text"][:500])