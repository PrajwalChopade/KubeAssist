def build_prompt(query, docs):

    context_parts = []

    for i, doc in enumerate(docs):

        if hasattr(doc, "payload"):
            text = doc.payload["text"]
        else:
            text = doc["text"]

        text = text[:1200]

        context_parts.append(
            f"[DOC {i+1}]\n{text}"
        )

    context = "\n\n".join(context_parts)

    return f"""
You are a Kubernetes expert.

Answer ONLY from the provided context.

Context:

{context}

Question:
{query}

Answer:
"""