from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams
)

COLLECTION_NAME = "kubernetes_docs"

client = QdrantClient(
    host="localhost",
    port=6333
)


def create_collection():

    existing = [
        c.name
        for c in client.get_collections().collections
    ]

    if COLLECTION_NAME in existing:

        print(
            f"{COLLECTION_NAME} already exists"
        )

        return

    client.create_collection(

        collection_name=
        COLLECTION_NAME,

        vectors_config=
        VectorParams(
            size=1024,
            distance=Distance.COSINE
        )
    )

    print(
        f"{COLLECTION_NAME} created"
    )


if __name__ == "__main__":

    create_collection()