
import io
import pandas as pd

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from database.storage import get_all_results


def generate_csv():

    results = get_all_results()

    dataframe = pd.DataFrame(results)

    if dataframe.empty:
        dataframe = pd.DataFrame(
            columns=[
                "model_name",
                "model_version",
                "test_id",
                "category",
                "score",
                "passed"
            ]
        )

    return dataframe.to_csv(index=False).encode("utf-8")


def generate_pdf():

    results = get_all_results()

    buffer = io.BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=landscape(A4)
    )

    styles = getSampleStyleSheet()

    elements = []

    # Report title
    elements.append(
        Paragraph(
            "TRUST-AI Evaluation Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 15))

    elements.append(
        Paragraph(
            "Responsible AI evaluation results - Demonstration report",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 20))

    # Summary
    total_tests = len(results)

    passed_tests = sum(
        1 for item in results if item["passed"]
    )

    failed_tests = total_tests - passed_tests

    average_score = (
        sum(item["score"] for item in results) / total_tests
        if total_tests else 0
    )

    summary = [
        ["Total Tests", "Passed", "Failed", "Average Score"],
        [
            str(total_tests),
            str(passed_tests),
            str(failed_tests),
            f"{average_score:.2f}"
        ]
    ]

    summary_table = Table(summary)

    summary_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("PADDING", (0, 0), (-1, -1), 8),
        ])
    )

    elements.append(summary_table)

    elements.append(Spacer(1, 20))

    # Evaluation details
    data = [[
        "Model",
        "Version",
        "Test ID",
        "Category",
        "Score",
        "Status"
    ]]

    for item in results:
        data.append([
            str(item["model_name"]),
            str(item["model_version"]),
            str(item["test_id"]),
            str(item["category"]),
            str(item["score"]),
            "PASS" if item["passed"] else "FAIL"
        ])

    if not results:
        elements.append(
            Paragraph(
                "No evaluation results available.",
                styles["Normal"]
            )
        )
    else:
        result_table = Table(data, repeatRows=1)

        result_table.setStyle(
            TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("PADDING", (0, 0), (-1, -1), 7),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ])
        )

        elements.append(result_table)

    document.build(elements)

    buffer.seek(0)

    return buffer.getvalue()
