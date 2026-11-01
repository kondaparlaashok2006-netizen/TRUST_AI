
from analytics.version_comparison import compare_versions


def detect_regression(old_version, new_version, threshold=5):

    comparison = compare_versions(old_version, new_version)

    # Do not make a decision without comparable data
    if comparison["status"] != "COMPARABLE":
        return {
            "status": "INSUFFICIENT_DATA",
            "message": comparison["message"]
        }

    difference = comparison["difference"]

    if difference <= -threshold:
        status = "REGRESSION"
        message = "The new model has significantly lower scores."

    elif difference < 0:
        status = "SMALL_DECREASE"
        message = "The new model score has decreased slightly."

    else:
        status = "NO_REGRESSION"
        message = "No decrease in the average score was detected."

    return {
        **comparison,
        "regression_status": status,
        "message": message,
        "threshold": threshold
    }
