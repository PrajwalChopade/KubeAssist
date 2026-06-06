from retrieval.multi_query import multi_query_search

docs = multi_query_search(
    "What is HPA?"
)

print(f"Retrieved {len(docs)} docs")

for doc in docs[:3]:

    print("=" * 50)

    if hasattr(doc, "payload"):
        print(doc.payload["text"][:500])
    else:
        print(doc["text"][:500])