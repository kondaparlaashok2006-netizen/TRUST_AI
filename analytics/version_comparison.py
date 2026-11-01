
from database.storage import get_all_results


def compare_versions(old_version, new_version):

    results = get_all_results()

    # Get results for the old model version
    old_results = {
        row["test_id"]: row
        for row in results
        if row["model_version"] == old_version
    }

    # Get results for the new model version
    new_results = {
        row["test_id"]: row
        for row in results
        if row["model_version"] == new_version
    }

    # Compare only common test cases
    common_ids = set(old_results) & set(new_results)

    if not common_ids:
        return {
            "status": "INSUFFICIENT_DATA",
            "message": "No matching test cases found."
        }

    old_average = sum(
        old_results[test_id]["score"]
        for test_id in common_ids
    ) / len(common_ids)

    new_average = sum(
        new_results[test_id]["score"]
        for test_id in common_ids
    ) / len(common_ids)

    difference = new_average - old_average

    return {
        "status": "COMPARABLE",
        "old_version": old_version,
        "new_version": new_version,
        "old_score": round(old_average, 2),
        "new_score": round(new_average, 2),
        "difference": round(difference, 2),
        "common_tests": len(common_ids)
    }
