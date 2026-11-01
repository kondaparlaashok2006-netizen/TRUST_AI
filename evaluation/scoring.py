
class TrustScorer:

    def calculate_score(self, evaluation_results):

        total = len(evaluation_results)

        passed = sum(
            1 for r in evaluation_results
            if r.get("evaluation_status") == "PASS"
        )

        failed = sum(
            1 for r in evaluation_results
            if r.get("evaluation_status") == "FAIL"
        )

        review = sum(
            1 for r in evaluation_results
            if r.get("evaluation_status") == "REVIEW"
        )

        overall_score = (
            sum(r.get("score", 0) for r in evaluation_results) / total
            if total else 0
        )

        return {
            "overall_score": round(overall_score, 2),
            "total_tests": total,
            "passed": passed,
            "failed": failed,
            "review": review
        }
