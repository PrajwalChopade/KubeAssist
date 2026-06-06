from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-m3")


def embed(text: str) -> list[float]:
    return model.encode(text, normalize_embeddings=True).tolist()
