import json
from pathlib import Path

from qdrant_client import QdrantClient
from qdrant_client.models import (
    PointStruct,
    Distance,
    VectorParams,
)

from ingestion.embedder import embed
from vectordb.qdrant_manager import COLLECTION_NAME

client = QdrantClient(
    host="localhost",
    port=6333
)


def ensure_collection():
    sample_vector = embed("test")

    if not client.collection_exists(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=len(sample_vector),
                distance=Distance.COSINE,
            ),
        )
        print(f"Created collection: {COLLECTION_NAME}")


def load_chunks(chunk_dir: Path) -> int:
    ensure_collection()

    points = []
    counter = 0

    for file in chunk_dir.glob("*.json"):
        data = json.loads(file.read_text(encoding="utf-8"))

        vector = embed(data["text"])

        points.append(
            PointStruct(
                id=counter,
                vector=vector,
                payload=data,
            )
        )

        counter += 1

        # Batch insert every 100 chunks
        if len(points) >= 100:
            client.upsert(
                collection_name=COLLECTION_NAME,
                points=points,
            )
            points = []

    # Insert remaining points
    if points:
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=points,
        )

    return counter


if __name__ == "__main__":
    CHUNK_DIR = Path("data/chunks")

    loaded = load_chunks(CHUNK_DIR)

    print(f"Loaded {loaded} chunks into '{COLLECTION_NAME}'")