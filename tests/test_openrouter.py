# tests/test_openrouter.py

from llm.openrouter_client import generate

print(
    generate(
        "What is Kubernetes?"
    )
)