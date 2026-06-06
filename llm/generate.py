from llm.openrouter_client import client
from llm.prompts import SYSTEM_PROMPT


def generate(query: str, context: str) -> str:
    response = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"""
Question:
{query}

Context:
{context}
""",
            },
        ],
    )

    return response.choices[0].message.content
