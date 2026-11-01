import json

from evaluation.evaluator import TrustEvaluator
from evaluation.scoring import TrustScorer


def main():

    evaluator = TrustEvaluator()
    scorer = TrustScorer()

    with open(
        "test_results.json",
        "r",
        encoding="utf-8"
    ) as file:

        test_results = json.load(file)

    evaluation_results = []

    for test in test_results:

        result = evaluator.evaluate(
            test_id=test.get("test_id", "UNKNOWN"),
            category=test.get("category", ""),
            prompt=test.get("prompt", ""),
            expected=test.get("expected", ""),
            actual=test.get("actual", "")
        )

        evaluation_results.append(result)

        print(
            f"{result['test_id']} | "
            f"{result['category']} | "
            f"{result['evaluation_status']} | "
            f"{result['score']}"
        )

    summary = scorer.calculate_score(
        evaluation_results
    )

    print("\nTRUST-AI EVALUATION SUMMARY")
    print("=" * 40)

    print(
        json.dumps(
            summary,
            indent=4
        )
    )

    with open(
        "evaluation_results.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            {
                "summary": summary,
                "results": evaluation_results
            },
            file,
            indent=4
        )

    print(
        "\nResults saved to evaluation_results.json"
    )


if __name__ == "__main__":
    main()