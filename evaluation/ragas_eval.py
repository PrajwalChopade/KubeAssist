import json
import pandas as pd

from datasets import Dataset
from datasets import Features
from datasets import Sequence
from datasets import Value

from ragas import evaluate

from ragas.metrics import (
    context_precision,
    context_recall,
    answer_relevancy,
    faithfulness
)

INPUT_FILE = "evaluation/generated_answers.json"


def run_evaluation():

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as f:
        data = json.load(f)

    rows = []

    for item in data:

        rows.append(
            {
                "question": str(
                    item["question"]
                ),

                "answer": str(
                    item["answer"]
                ),

                "contexts": [
                    str(context)
                    for context in item["contexts"]
                ],

                "ground_truth": str(
                    item["ground_truth"]
                )
            }
        )

    df = pd.DataFrame(rows)

    print("\nDataFrame Types:")
    print(df.dtypes)

    features = Features(
        {
            "question": Value("string"),
            "answer": Value("string"),
            "contexts": Sequence(
                Value("string")
            ),
            "ground_truth": Value(
                "string"
            )
        }
    )

    dataset = Dataset.from_pandas(
        df,
        features=features,
        preserve_index=False
    )

    print("\nDataset Features:")
    print(dataset.features)

    print("\nSample Record:")
    print(dataset[0])

    result = evaluate(
        dataset=dataset,
        metrics=[
            context_precision,
            context_recall,
            answer_relevancy,
            faithfulness
        ]
    )

    print("\n")
    print("=" * 60)
    print("RAGAS EVALUATION RESULTS")
    print("=" * 60)

    print(result)

    with open(
        "evaluation/results.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(
            str(result)
        )

    print(
        "\nResults saved to evaluation/results.txt"
    )


if __name__ == "__main__":
    run_evaluation()