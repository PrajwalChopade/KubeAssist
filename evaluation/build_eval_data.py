import json

from rag.query_engine import ask_with_context

INPUT_FILE = "evaluation/eval_dataset.json"
OUTPUT_FILE = "evaluation/generated_answers.json"


def build_dataset():

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        questions = json.load(f)

    results = []

    for item in questions:

        question = item["question"]

        print(f"Evaluating: {question}")

        result = ask_with_context(
            question
        )

        results.append(
            {
                "question":
                    question,

                "answer":
                    result["answer"],

                "contexts":
                    result["contexts"],

                "ground_truth":
                    item["ground_truth"]
            }
        )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            results,
            f,
            indent=4,
            ensure_ascii=False
        )

    print(
        f"Generated {len(results)} examples"
    )


if __name__ == "__main__":
    build_dataset()