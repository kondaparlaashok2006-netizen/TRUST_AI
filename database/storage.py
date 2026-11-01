
from database.db import get_connection, initialize_database


def save_results(results):
    initialize_database()
    connection = get_connection()

    query = """
    INSERT INTO evaluation_results (
        run_id, model_name, model_version, test_id,
        category, score, passed, input_prompt,
        model_output, evidence
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ON CONFLICT(run_id, test_id)
    DO UPDATE SET
        score = excluded.score,
        passed = excluded.passed,
        model_output = excluded.model_output,
        evidence = excluded.evidence
    """

    try:
        for item in results:
            values = (
                item["run_id"],
                item["model_name"],
                item["model_version"],
                item["test_id"],
                item.get("category", "General"),
                float(item.get("score", 0)),
                int(bool(item.get("passed", False))),
                item.get("input_prompt", ""),
                item.get("model_output", ""),
                item.get("evidence", "")
            )

            connection.execute(query, values)

        connection.commit()

    finally:
        connection.close()


def get_all_results():
    initialize_database()
    connection = get_connection()

    try:
        rows = connection.execute(
            "SELECT * FROM evaluation_results ORDER BY created_at DESC"
        ).fetchall()

        return [dict(row) for row in rows]

    finally:
        connection.close()


def get_results_by_version(version):
    initialize_database()
    connection = get_connection()

    try:
        rows = connection.execute(
            "SELECT * FROM evaluation_results WHERE model_version = ?",
            (version,)
        ).fetchall()

        return [dict(row) for row in rows]

    finally:
        connection.close()
