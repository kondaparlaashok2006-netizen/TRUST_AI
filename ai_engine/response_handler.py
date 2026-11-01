"""
TRUST-AI Response Handler

Normalizes Gemini responses and prepares structured results.
"""


def normalize_response(response):

    if response is None:

        return ""

    if not isinstance(response, str):

        response = str(response)

    response = response.strip()

    return response


def create_result(
    test_case,
    actual,
    model_name,
    version,
    status="COMPLETED",
    error=None
):

    normalized_actual = normalize_response(actual)

    result = {

        "test_id": test_case["test_id"],

        "category": test_case["category"],

        "prompt": test_case["prompt"],

        "expected": test_case["expected"],

        "actual": normalized_actual,

        "model": model_name,

        "version": version,

        "status": status,

        "error": error

    }

    return result


def create_error_result(
    test_case,
    model_name,
    version,
    error_message
):

    return create_result(

        test_case=test_case,

        actual="",

        model_name=model_name,

        version=version,

        status="FAILED",

        error=error_message

    )