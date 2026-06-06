# tests/test_embed.py

from ingestion.embedder import embed

vec = embed("What is Kubernetes?")

print(type(vec))
print(len(vec))