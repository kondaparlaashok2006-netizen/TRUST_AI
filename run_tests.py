"""
TRUST-AI Main Test Execution Script

Runs the AI integration test suite.
"""


import json

import os

from dotenv import load_dotenv

from ai_engine.test_cases import load_test_cases

from ai_engine.test_runner import run_test_suite


# Load environment configuration
load_dotenv()


# Read model configuration
MODEL_NAME = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")

# Read version
VERSION = os.getenv(
    "TRUST_AI_VERSION",
    "V1"
)


def main():

    print("\nStarting TRUST-AI AI Integration...\n")


    # Load test cases
    test_cases = load_test_cases()


    # Run tests
    results = run_test_suite(

        test_cases=test_cases,

        model_name=MODEL_NAME,

        version=VERSION

    )


    # Save results to JSON
    with open(
        "test_results.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(

            results,

            file,

            indent=4,

            ensure_ascii=False

        )


    print(
        "\nResults saved to test_results.json"
    )


if __name__ == "__main__":

    main()