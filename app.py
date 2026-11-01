
import streamlit as st

from frontend.styles import (
    apply_custom_styles,
    render_page_header
)

from frontend.navigation import show_navigation

from frontend.configuration_ui import (
    show_configuration,
    show_test_configuration
)

from frontend.custom_testing_ui import show_custom_testing

from frontend.results_ui import (
    show_results,
    show_version_comparison,
    show_reports,
    get_sample_results
)


# =========================================
# PAGE CONFIGURATION
# =========================================

st.set_page_config(
    page_title="TRUST-AI",
    page_icon="🛡️",
    layout="wide"
)


# =========================================
# CUSTOM STYLES
# =========================================

apply_custom_styles()


# =========================================
# NAVIGATION
# =========================================

current_page = show_navigation()


# =========================================
# DASHBOARD PAGE
# =========================================

if current_page == "Dashboard":

    render_page_header(
        "TRUST-AI Dashboard",
        "Responsible AI Output Evaluation Platform"
    )

    history = st.session_state.get(
        "custom_test_history",
        []
    )

    total_tests = len(history)

    passed = sum(
        1 for item in history
        if item["evaluation"]["evaluation_status"] == "PASS"
    )

    failed = sum(
        1 for item in history
        if item["evaluation"]["evaluation_status"] == "FAIL"
    )

    review = sum(
        1 for item in history
        if item["evaluation"]["evaluation_status"] == "REVIEW"
    )

    average_score = (
        sum(
            item["evaluation"]["score"]
            for item in history
        ) / total_tests
        if total_tests else 0
    )

    st.subheader("Evaluation Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Tests",
        total_tests
    )

    col2.metric(
        "Passed",
        passed
    )

    col3.metric(
        "Failed",
        failed
    )

    col4.metric(
        "Review",
        review
    )

    st.metric(
        "Average Trust Score",
        f"{average_score:.1f}/100"
    )

    st.divider()

    st.subheader("Welcome to TRUST-AI")

    st.write(
        """
        TRUST-AI evaluates AI-generated responses for
        responsible and trustworthy AI behavior.

        You can configure your AI model, ask custom questions,
        evaluate its responses, and generate reports.
        """
    )

    if st.button(
        "Start Custom Question Testing",
        type="primary"
    ):

        st.session_state["current_page"] = (
            "Custom Question Testing"
        )

        st.rerun()


# =========================================
# MODEL CONFIGURATION
# =========================================

elif current_page == "Model Configuration":

    show_configuration()


# =========================================
# TEST CONFIGURATION
# =========================================

elif current_page == "Test Configuration":

    show_test_configuration()


# =========================================
# CUSTOM QUESTION TESTING
# =========================================

elif current_page == "Custom Question Testing":

    show_custom_testing()


# =========================================
# EVALUATION RESULTS
# =========================================

elif current_page == "Evaluation Results":

    history = st.session_state.get(
        "custom_test_history",
        []
    )

    if history:

        render_page_header(
            "Evaluation Results",
            "Results from your custom AI tests."
        )

        rows = []

        for item in history:

            evaluation = item["evaluation"]

            rows.append({
                "Test ID": item["test_id"],
                "Question": item["question"],
                "Category": item["category"],
                "Score": evaluation["score"],
                "Status": evaluation["evaluation_status"]
            })

        st.dataframe(
            rows,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No custom evaluation results available. "
            "Run a custom test first."
        )


# =========================================
# VERSION COMPARISON
# =========================================

elif current_page == "Version Comparison":

    show_version_comparison(None)


# =========================================
# REPORTS
# =========================================

elif current_page == "Reports":

    history = st.session_state.get(
        "custom_test_history",
        []
    )

    render_page_header(
        "Reports",
        "Download your custom evaluation results."
    )

    if history:

        import json
        import pandas as pd

        report_json = json.dumps(
            history,
            indent=4
        )

        st.download_button(
            "Download JSON Report",
            data=report_json,
            file_name="trust_ai_report.json",
            mime="application/json"
        )

        report_rows = []

        for item in history:

            evaluation = item["evaluation"]

            report_rows.append({
                "Test ID": item["test_id"],
                "Question": item["question"],
                "Category": item["category"],
                "Score": evaluation["score"],
                "Status": evaluation["evaluation_status"]
            })

        report_df = pd.DataFrame(report_rows)

        st.download_button(
            "Download CSV Report",
            data=report_df.to_csv(index=False),
            file_name="trust_ai_report.csv",
            mime="text/csv"
        )

    else:

        st.info(
            "Run at least one custom test before downloading reports."
        )
