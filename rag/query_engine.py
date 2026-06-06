from retrieval.hybrid import hybrid_search
from retrieval.reranker import rerank

from llm.prompt_builder import build_prompt
from llm.openrouter_client import generate
from cache.semantic_cache import (
    get_cached_answer,
    save_answer
)
from retrieval.multi_query import (
    multi_query_search
)
# def ask(query):

#     docs = hybrid_search(
#         query,
#         top_k=20
#     )

#     docs = rerank(
#         query,
#         docs,
#         top_k=3
#     )

#     prompt = build_prompt(
#         query,
#         docs
#     )

#     answer = generate(prompt)

#     sources = []

#     for doc in docs:

#         if hasattr(doc, "payload"):

#             source = doc.payload.get(
#                 "source",
#                 "unknown"
#             )

#         else:

#             source = doc.get(
#                 "source",
#                 "unknown"
#             )

#         sources.append(source)

#     return {
#         "answer": answer,
#         "sources": list(set(sources))
#     }

def ask(query):

    cached = get_cached_answer(query)

    if cached:

        return {
            "answer": cached,
            "sources": ["semantic_cache"]
        }

    docs = multi_query_search(
        query,
        top_k=20
    )

    docs = rerank(
        query,
        docs,
        top_k=5
    )

    prompt = build_prompt(
        query,
        docs
    )

    answer = generate(prompt)

    save_answer(
        query,
        answer
    )

    return {
        "answer": answer,
        "sources": []
    }


def ask_with_context(query):

    docs = multi_query_search(
        query,
        top_k=20
    )

    docs = rerank(
        query,
        docs,
        top_k=5
    )

    contexts = []

    for doc in docs:

        if hasattr(doc, "payload"):
            contexts.append(
                doc.payload["text"]
            )
        else:
            contexts.append(
                doc["text"]
            )

    prompt = build_prompt(
        query,
        docs
    )

    answer = generate(prompt)

    return {
        "answer": answer,
        "contexts": contexts
    }