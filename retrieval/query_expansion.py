EXPANSIONS = {
    "hpa": [
        "horizontal pod autoscaler",
        "autoscaling"
    ],
    "deployment": [
        "replicaset",
        "deployment controller",
        "rollout"
    ],
    "service": [
        "cluster ip",
        "load balancer",
        "networking"
    ],
    "pv": [
        "persistent volume",
        "storage"
    ],
    "pvc": [
        "persistent volume claim",
        "storage request"
    ],
    "ingress": [
        "http routing",
        "load balancing"
    ]
}

def expand_query(query: str):

    expanded_queries = [query]

    lowered = query.lower()

    for key, values in EXPANSIONS.items():

        if key in lowered:

            expanded_queries.extend(values)

    return list(set(expanded_queries))