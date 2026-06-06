import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

MODEL = "qwen/qwen3-8b"
# MODEL = "google/gemma-3-4b-it:free"


def generate(prompt):

    response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.1,
    max_tokens=512
)
    return response.choices[0].message.content