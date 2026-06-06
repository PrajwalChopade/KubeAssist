from sentence_transformers import CrossEncoder

model = CrossEncoder(
    "BAAI/bge-reranker-v2-m3",
    trust_remote_code=True
)

def rerank(query, docs, top_k=5):

    pairs = []

    for doc in docs:

        if hasattr(doc, "payload"):
            text = doc.payload["text"]
        else:
            text = doc["text"]

        pairs.append((query, text))

    scores = model.predict(pairs)

    ranked = sorted(
        zip(scores, docs),
        key=lambda x: x[0],
        reverse=True
    )

    return [
        item[1]
        for item in ranked[:top_k]
    ]