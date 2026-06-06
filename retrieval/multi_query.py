from retrieval.query_expansion import expand_query
from retrieval.hybrid import hybrid_search


def multi_query_search(query, top_k=20):

    expanded_queries = expand_query(query)

    all_results = []
    seen = set()

    print("Expanded Queries:")
    print(expanded_queries)

    for q in expanded_queries:

        results = hybrid_search(
            q,
            top_k=10
        )

        for doc in results:

            if hasattr(doc, "payload"):
                chunk_id = doc.payload["chunk_id"]
            else:
                chunk_id = doc["chunk_id"]

            if chunk_id not in seen:
                seen.add(chunk_id)
                all_results.append(doc)

    return all_results[:top_k]