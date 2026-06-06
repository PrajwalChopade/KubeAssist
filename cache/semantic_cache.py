import json
import redis
import numpy as np

from ingestion.embedder import embed

SIMILARITY_THRESHOLD = 0.95

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


def cosine_similarity(a, b):

    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a)
        * np.linalg.norm(b)
    )


def get_cached_answer(query):

    query_embedding = embed(query)

    keys = redis_client.keys("cache:*")

    for key in keys:

        item = json.loads(
            redis_client.get(key)
        )

        similarity = cosine_similarity(
            query_embedding,
            item["embedding"]
        )

        if similarity >= SIMILARITY_THRESHOLD:

            print(
                f"Cache HIT ({similarity:.3f})"
            )

            return item["answer"]

    print("Cache MISS")

    return None


def save_answer(
    query,
    answer
):

    embedding = embed(query)

    payload = {
        "query": query,
        "answer": answer,
        "embedding": embedding
    }

    redis_client.set(
        f"cache:{query}",
        json.dumps(payload)
    )