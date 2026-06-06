# from qdrant_client import QdrantClient

# from ingestion.embedder import embed

# # from qdrant_client import QdrantClient

# client = QdrantClient(
#     host="localhost",
#     port=6333
# )
# # python -c "from qdrant_client import QdrantClient;c=QdrantClient(host="localhost",port=6333);print(c.count(collection_name='kubernetes_docs', exact=True))"
# # python -c "from qdrant_client import QdrantClient;c=QdrantClient(path='./qdrant_data');print(c.count(collection_name='kubernetes_docs', exact=True))"
# def dense_search(query: str, top_k: int = 20):
#     query_vector = embed(query)

#     results = client.search(
#         collection_name="kubernetes_docs",
#         query_vector=query_vector,
#         limit=top_k,
#     )

#     return results


from qdrant_client import QdrantClient
from ingestion.embedder import embed

client = QdrantClient(
    host="localhost",
    port=6333
)

COLLECTION_NAME = "kubernetes_docs"

def dense_search(query, top_k=5):

    query_vector = embed(query)

    result = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k
    )

    return result.points