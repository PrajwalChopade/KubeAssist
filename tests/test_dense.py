# tests/test_dense.py

from retrieval.dense import dense_search

results = dense_search(
    "What is a Deployment?"
)

for r in results:
    print("=" * 100)
    print(r.payload["text"][:1000])
# from retrieval.dense import dense_search

# results = dense_search(
#     "What is a Deployment?"
# )

# for r in results:
#     print("=" * 100)
#     print("Chunk:", r.payload["chunk_id"])
#     print()
#     print(r.payload["text"][:1000])