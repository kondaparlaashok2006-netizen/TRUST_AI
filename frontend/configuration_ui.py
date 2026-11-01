import streamlit as st
from frontend.styles import render_page_header

MODEL_OPTIONS = ["OpenAI GPT", "Google Gemini", "Meta Llama", "Anthropic Claude", "Custom Model"]

def show_configuration():
    render_page_header("Model Configuration", "Choose the model and define the prompt to evaluate.")
    st.info("Frontend configuration only. API connectivity is not verified by this page.")
    saved = st.session_state.get("model_config", {})
    with st.form("model_configuration_form"):
        col1, col2 = st.columns(2)
        with col1:
            provider = st.selectbox("Model provider", MODEL_OPTIONS,
                index=MODEL_OPTIONS.index(saved.get("provider", MODEL_OPTIONS[0])))
            model_name = st.text_input("Model name / identifier", value=saved.get("model_name", ""))
        with col2:
            version = st.text_input("Model version", value=saved.get("version", ""))
            api_status = st.selectbox("API setup status", ["Not configured", "Configured (not verified)"],
                index=1 if saved.get("api_status") == "Configured (not verified)" else 0)
        prompt = st.text_area("Evaluation prompt / system instruction",
            value=saved.get("prompt", ""),
            placeholder="Enter the prompt or instruction that will be evaluated...", height=180)
        submitted = st.form_submit_button("Save Model Configuration", use_container_width=True)
    if submitted:
        if not model_name.strip():
            st.error("Enter a model name or identifier.")
        elif not prompt.strip():
            st.error("Enter the prompt to evaluate.")
        else:
            st.session_state["model_config"] = {
                "provider": provider, "model_name": model_name.strip(),
                "version": version.strip(), "api_status": api_status,
                "prompt": prompt.strip()
            }
            st.success("Model configuration saved in this Streamlit session.")
    if st.session_state.get("model_config"):
        st.caption("Saved configuration is available in st.session_state['model_config'].")

def show_test_configuration():
    render_page_header("Test Configuration", "Select responsible-AI checks and evaluation strictness.")
    saved = st.session_state.get("test_config", {})
    with st.form("test_configuration_form"):
        tests = st.multiselect(
            "Evaluation dimensions",
            ["Hallucination", "Bias", "Citation Quality", "Security", "Privacy", "Toxicity"],
            default=saved.get("tests", ["Hallucination", "Bias", "Citation Quality", "Security"])
        )
        strictness = st.select_slider("Evaluation strictness",
            options=["Low", "Medium", "High"],
            value=saved.get("strictness", "Medium"))
        threshold = st.slider("Passing score threshold", 0, 100,
            value=int(saved.get("threshold", 70)))
        submitted = st.form_submit_button("Save Test Configuration", use_container_width=True)
    if submitted:
        if not tests:
            st.error("Select at least one evaluation dimension.")
        else:
            st.session_state["test_config"] = {
                "tests": tests, "strictness": strictness, "threshold": threshold
            }
            st.success("Test configuration saved in this Streamlit session.")
    st.warning("Saving settings does not run an evaluation. The evaluation engine must be connected by the backend team.")
