"""
TRUST-AI Test Runner

Loads test cases, sends prompts to Gemini,
and collects structured results.
"""


from ai_engine.gemini_client import generate_response

from ai_engine.test_cases import load_test_cases

from ai_engine.response_handler import (
    create_result,
    create_error_result
)


def run_test_suite(
    test_cases,
    model_name,
    version
):
    """
    Executes a test suite against Gemini.

    Args:
        test_cases: List of test case dictionaries.
        model_name: Gemini model identifier.
        version: TRUST-AI evaluation version.

    Returns:
        List of structured result dictionaries.
    """

    results = []

    print("\n")
    print("=" * 60)

    print("TRUST-AI TEST RUNNER")

    print("=" * 60)

    print(f"Model: {model_name}")

    print(f"Version: {version}")

    print(f"Total Tests: {len(test_cases)}")

    print("=" * 60)


    for index, test_case in enumerate(
        test_cases,
        start=1
    ):

        test_id = test_case["test_id"]

        category = test_case["category"]

        prompt = test_case["prompt"]


        print("\n")

        print(
            f"[{index}/{len(test_cases)}] "
            f"Running Test: {test_id}"
        )

        print(
            f"Category: {category}"
        )


        try:

            # Send prompt to Gemini
            actual = generate_response(prompt)


            # Prepare successful result
            result = create_result(

                test_case=test_case,

                actual=actual,

                model_name=model_name,

                version=version,

                status="COMPLETED",

                error=None

            )


            print("Status: COMPLETED")


        except Exception as error:

            # Never fabricate a response
            result = create_error_result(

                test_case=test_case,

                model_name=model_name,

                version=version,

                error_message=str(error)

            )


            print("Status: FAILED")

            print(
                f"Error: {error}"
            )


        results.append(result)


    print("\n")

    print("=" * 60)

    print("TEST EXECUTION COMPLETED")

    print("=" * 60)


    completed = sum(

        1 for result in results

        if result["status"] == "COMPLETED"

    )


    failed = sum(

        1 for result in results

        if result["status"] == "FAILED"

    )


    print(f"Completed: {completed}")

    print(f"Failed: {failed}")

    print(f"Total: {len(results)}")


    return results


def load_and_run_tests(
    model_name,
    version
):
    """
    Loads the predefined test cases
    and executes the test suite.
    """

    test_cases = load_test_cases()

    results = run_test_suite(

        test_cases=test_cases,

        model_name=model_name,

        version=version

    )

    return results