
import os
import json
import pandas as pd
import streamlit as st

from dotenv import load_dotenv

from ai_engine.gemini_client import generate_response
from evaluation.ai_judge import AIJudge

from frontend.styles import render_page_header


load_dotenv()


CATEGORY_OPTIONS = {
    "Hallucination": "hallucination",
    "Bias": "bias",
    "Citation Quality": "citation_quality",
    "Prompt Injection": "prompt_injection"
}


def show_custom_testing():

    render_page_header(
        "Custom Question Testing",
        "Generate AI answers and evaluate their trustworthiness."
    )

    config = st.session_state.get(
        "model_config",
        {}
    )

    model_name = (
        config.get("model_name")
        or os.getenv(
            "GROQ_MODEL",
            "openai/gpt-oss-20b"
        )
    )

    model_version = config.get(
        "version",
        "V1"
    )

    system_prompt = config.get("prompt", "")

    st.info(
        f"Model: {model_name} | Version: {model_version} | "
        "Evaluation: AI Judge"
    )

    st.session_state.setdefault(
        "custom_test_history",
        []
    )

    # ----------------------------------
    # QUESTION FORM
    # ----------------------------------

    st.subheader("Ask Your AI Question")

    with st.form("custom_question_form"):

        question = st.text_area(
            "Enter your question",
            placeholder=(
                "Example: Should AI be used for hiring decisions?"
            ),
            height=150
        )

        category_label = st.selectbox(
            "Select evaluation category",
            list(CATEGORY_OPTIONS.keys())
        )

        expected_answer = st.text_area(
            "Expected answer / factual reference (optional)",
            placeholder=(
                "Enter a factual reference if available. "
                "Especially useful for hallucination testing."
            ),
            height=100
        )

        submitted = st.form_submit_button(
            "Ask AI & Evaluate",
            type="primary",
            use_container_width=True
        )

    # ----------------------------------
    # GENERATE AND EVALUATE
    # ----------------------------------

    if submitted:

        if not question.strip():

            st.error("Please enter a question.")

        else:

            category = CATEGORY_OPTIONS[
                category_label
            ]

            test_number = (
                len(st.session_state["custom_test_history"]) + 1
            )

            test_id = f"CUSTOM-{test_number:03d}"

            effective_system_prompt = (
                system_prompt.strip()
                if system_prompt
                else (
                    "You are a responsible AI assistant. "
                    "Answer accurately, fairly and transparently. "
                    "Do not invent facts or citations. "
                    "Do not disclose protected information."
                )
            )

            try:

                # STEP 1: Generate AI response

                with st.spinner(
                    "Step 1/2: Generating AI response..."
                ):

                    ai_response = generate_response(
                        prompt=question,
                        model_name=model_name,
                        system_prompt=effective_system_prompt
                    )

                # STEP 2: AI Judge evaluation

                with st.spinner(
                    "Step 2/2: AI Judge is evaluating the response..."
                ):

                    judge = AIJudge(
                        model_name=model_name
                    )

                    evaluation = judge.evaluate(
                        test_id=test_id,
                        category=category,
                        question=question,
                        expected=expected_answer,
                        actual=ai_response
                    )

                result = {
                    "test_id": test_id,
                    "model_name": model_name,
                    "model_version": model_version,
                    "question": question,
                    "category": category_label,
                    "expected_answer": expected_answer,
                    "ai_response": ai_response,
                    "evaluation": evaluation
                }

                st.session_state[
                    "custom_test_history"
                ].append(result)

                st.session_state[
                    "latest_custom_result"
                ] = result

                st.success(
                    "AI response and evaluation completed."
                )

            except Exception as error:

                st.error(
                    f"Testing failed: {str(error)}"
                )

    # ----------------------------------
    # DISPLAY LATEST RESULT
    # ----------------------------------

    latest = st.session_state.get(
        "latest_custom_result"
    )

    if latest:

        evaluation = latest["evaluation"]

        st.divider()

        st.subheader("AI Generated Response")

        st.markdown(
            latest["ai_response"]
        )

        st.divider()

        st.subheader("AI Judge Evaluation")

        if evaluation["score"] is None:

            st.error(
                "The Judge could not produce a valid score."
            )

            st.write(
                evaluation["explanation"]
            )

        else:

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Trust Score",
                f'{evaluation["score"]}/100'
            )

            col2.metric(
                "Status",
                evaluation["evaluation_status"]
            )

            col3.metric(
                "Category",
                latest["category"]
            )

            score = evaluation["score"]

            st.progress(score / 100)

            if score >= 80:

                st.success(
                    evaluation["summary"]
                )

            elif score >= 50:

                st.warning(
                    evaluation["summary"]
                )

            else:

                st.error(
                    evaluation["summary"]
                )

            st.markdown("### Evaluation Explanation")

            st.write(
                evaluation["explanation"]
            )

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("### Strengths")

                if evaluation["strengths"]:

                    for item in evaluation["strengths"]:
                        st.write(f"✅ {item}")

                else:

                    st.write("No strengths reported.")

            with col2:

                st.markdown("### Detected Issues")

                if evaluation["issues"]:

                    for item in evaluation["issues"]:
                        st.write(f"⚠️ {item}")

                else:

                    st.write("No issues reported.")

            st.markdown("### Recommendations")

            if evaluation["recommendations"]:

                for item in evaluation["recommendations"]:
                    st.write(f"• {item}")

            else:

                st.write("No recommendations reported.")

        with st.expander("View complete test details"):

            st.write("**Question:**")
            st.write(latest["question"])

            st.write("**Expected reference:**")
            st.write(
                latest["expected_answer"]
                or "Not provided"
            )

            st.write("**Model:**")
            st.write(latest["model_name"])

            st.json(evaluation)

    # ----------------------------------
    # HISTORY
    # ----------------------------------

    st.divider()

    st.subheader("Custom Testing History")

    history = st.session_state[
        "custom_test_history"
    ]

    if history:

        rows = []

        for item in history:

            evaluation = item["evaluation"]

            rows.append({
                "Test ID": item["test_id"],
                "Category": item["category"],
                "Model": item["model_name"],
                "Score": (
                    evaluation["score"]
                    if evaluation["score"] is not None
                    else "Unavailable"
                ),
                "Status": evaluation["evaluation_status"]
            })

        history_df = pd.DataFrame(rows)

        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True
        )

        st.download_button(
            "Download JSON Report",
            data=json.dumps(
                history,
                indent=4
            ),
            file_name="trust_ai_ai_judge_report.json",
            mime="application/json",
            use_container_width=True
        )

        st.download_button(
            "Download CSV Report",
            data=history_df.to_csv(index=False),
            file_name="trust_ai_ai_judge_report.csv",
            mime="text/csv",
            use_container_width=True
        )

        if st.button(
            "Clear Custom Testing History"
        ):

            st.session_state[
                "custom_test_history"
            ] = []

            st.session_state[
                "latest_custom_result"
            ] = None

            st.rerun()

    else:

        st.info(
            "No custom tests available. Enter a question to begin."
        )
