import streamlit as st
import pandas as pd
import plotly.express as px

from frontend.styles import apply_custom_styles, render_page_header
from frontend.navigation import show_navigation
from frontend.configuration_ui import show_configuration, show_test_configuration
from frontend.results_ui import (
    show_results, show_version_comparison, show_reports, get_sample_results
)

def get_dashboard_sample_data():
    return {
        "total_evaluations": 128,
        "average_trust_score": 87.5,
        "passed_tests": 106,
        "failed_tests": 22,
        "trend": pd.DataFrame({
            "Date": ["Oct 25", "Oct 26", "Oct 27", "Oct 28", "Oct 29", "Oct 30", "Oct 31"],
            "Trust Score": [76, 81, 79, 84, 82, 88, 87.5]
        }),
        "activity": pd.DataFrame({
            "Evaluation": ["GPT example", "Gemini example", "Llama example", "Claude example"],
            "Category": ["All Tests", "Bias", "Security", "Hallucination"],
            "Score": [92, 85, 78, 89],
            "Status": ["PASS", "PASS", "FAIL", "PASS"],
            "Date": ["Oct 31", "Oct 30", "Oct 29", "Oct 28"]
        })
    }

def show_dashboard():
    data = get_dashboard_sample_data()
    render_page_header("TRUST-AI Dashboard", "Monitor AI trustworthiness, evaluation performance and risks.")
    st.warning("DEVELOPMENT PREVIEW: Dashboard metrics and charts use illustrative sample data.")
    st.subheader("Evaluation Overview")
    cols = st.columns(4)
    cols[0].metric("Total Evaluations", data["total_evaluations"])
    cols[1].metric("Average Trust Score", f'{data["average_trust_score"]}/100')
    cols[2].metric("Passed Tests", data["passed_tests"])
    cols[3].metric("Failed Tests", data["failed_tests"])
    st.divider()
    st.subheader("Trust Score Analytics")
    fig = px.line(data["trend"], x="Date", y="Trust Score", markers=True)
    fig.update_traces(line_color="#E10600", marker_color="#C0C0C0", line_width=3)
    fig.update_layout(paper_bgcolor="#333333", plot_bgcolor="#333333",
                      font_color="#F5F5F5", yaxis_range=[0, 105], height=340)
    st.plotly_chart(fig, use_container_width=True)
    st.divider()
    st.subheader("Recent Evaluation Activity")
    st.dataframe(data["activity"], use_container_width=True, hide_index=True)
    st.caption("All records above are illustrative sample data.")

def route_page(page):
    if page == "Dashboard":
        show_dashboard()
    elif page == "Model Configuration":
        show_configuration()
    elif page == "Test Configuration":
        show_test_configuration()
    elif page == "Evaluation Results":
        show_results(st.session_state.get("evaluation_results", get_sample_results()))
    elif page == "Version Comparison":
        show_version_comparison(st.session_state.get("comparison_data", {}))
    elif page == "Reports":
        show_reports(st.session_state.get("evaluation_results", get_sample_results()))
    else:
        st.error("Unknown page. Showing dashboard.")
        show_dashboard()

def main():
    st.set_page_config(
        page_title="TRUST-AI | Responsible AI Dashboard",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    apply_custom_styles()
    selected_page = show_navigation()
    route_page(selected_page)

if __name__ == "__main__":
    main()
