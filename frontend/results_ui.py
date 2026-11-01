import io
import json
import pandas as pd
import plotly.express as px
import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from frontend.styles import render_page_header

def get_sample_results():
    return {
        "is_sample": True,
        "model_name": "Example model",
        "overall_score": 82,
        "status": "SAMPLE",
        "categories": [
            {"name": "Hallucination", "score": 88, "status": "PASS", "details": "Illustrative result only."},
            {"name": "Bias", "score": 72, "status": "PASS", "details": "Illustrative result only."},
            {"name": "Citation Quality", "score": 65, "status": "FAIL", "details": "Illustrative result only."},
            {"name": "Security", "score": 91, "status": "PASS", "details": "Illustrative result only."},
        ],
    }

def normalize_results(results):
    if not isinstance(results, dict):
        return get_sample_results()
    normalized = dict(results)
    normalized.setdefault("model_name", "Unknown model")
    normalized.setdefault("overall_score", 0)
    normalized.setdefault("status", "UNKNOWN")
    normalized.setdefault("categories", [])
    normalized.setdefault("is_sample", False)
    return normalized

def show_results(results):
    data = normalize_results(results)
    render_page_header("Evaluation Results", "Review model trust scores and dimension-level findings.")
    if data["is_sample"]:
        st.warning("SAMPLE DATA: These results are illustrative, not produced by a real evaluation.")
    c1, c2, c3 = st.columns(3)
    c1.metric("Overall trust score", f'{data["overall_score"]}/100')
    c2.metric("Model", data["model_name"])
    c3.metric("Status", data["status"])
    categories = data["categories"]
    if categories:
        df = pd.DataFrame(categories)
        required = {"name", "score"}
        if required.issubset(df.columns):
            fig = px.bar(df, x="name", y="score", range_y=[0, 100], color="score",
                         color_continuous_scale=["#777777", "#C0C0C0", "#E10600"])
            fig.update_layout(paper_bgcolor="#333333", plot_bgcolor="#333333",
                              font_color="#F5F5F5", coloraxis_showscale=False)
            st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("No category-level results are available yet.")

def show_version_comparison(comparison_data):
    render_page_header("Version Comparison", "Compare two model versions using evaluation results.")
    if not comparison_data:
        st.info("No comparison data is connected yet. Backend integration is required.")
        return
    st.json(comparison_data)

def _report_dataframe(report_data):
    data = normalize_results(report_data)
    return pd.DataFrame(data["categories"]), data

def generate_pdf_report(report_data):
    df, data = _report_dataframe(report_data)
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 55
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(45, y, "TRUST-AI Evaluation Report")
    y -= 30
    pdf.setFont("Helvetica", 11)
    pdf.drawString(45, y, f'Model: {data["model_name"]}')
    y -= 18
    pdf.drawString(45, y, f'Overall score: {data["overall_score"]}/100')
    y -= 18
    pdf.drawString(45, y, f'Sample data: {data["is_sample"]}')
    y -= 30
    for _, row in df.iterrows():
        line = f'{row.get("name", "Category")}: {row.get("score", "N/A")} - {row.get("status", "N/A")}'
        pdf.drawString(45, y, line[:100])
        y -= 18
        if y < 55:
            pdf.showPage()
            y = height - 55
            pdf.setFont("Helvetica", 11)
    pdf.save()
    buffer.seek(0)
    return buffer.getvalue()

def show_reports(report_data):
    render_page_header("Reports", "Export evaluation findings for sharing and review.")
    df, data = _report_dataframe(report_data)
    if data["is_sample"]:
        st.warning("The current report uses sample data. Replace it with backend results before presenting it as a real evaluation.")
    report = {
        "model_name": data["model_name"],
        "overall_score": data["overall_score"],
        "status": data["status"],
        "is_sample": data["is_sample"],
        "categories": data["categories"],
    }
    st.download_button("Download JSON report", json.dumps(report, indent=2),
                       file_name="trust_ai_report.json", mime="application/json",
                       use_container_width=True)
    st.download_button("Download CSV results", df.to_csv(index=False),
                       file_name="trust_ai_results.csv", mime="text/csv",
                       use_container_width=True)
    st.download_button("Download PDF report", generate_pdf_report(report_data),
                       file_name="trust_ai_report.pdf", mime="application/pdf",
                       use_container_width=True)
