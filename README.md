# TRUST-AI Frontend Starter

A Streamlit frontend starter for the TRUST-AI Responsible AI Output Evaluation Dashboard.

## Included
- Dashboard with clearly labeled illustrative sample metrics
- Model configuration form
- Test configuration form
- Evaluation results view
- Version comparison placeholder
- JSON, CSV, and PDF report downloads
- Charcoal / silver / signal-red theme and Josefin Sans typography
- Sidebar navigation with Streamlit Material icons

## Windows quick start

1. Extract this ZIP into your project folder.
2. Open PowerShell in the extracted folder.
3. Run:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run frontend\dashboard.py
```

If PowerShell blocks activation, run this once in that terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Alternatively, double-click `run.bat`.

## Important integration contract for backend developer

Frontend stores these values in Streamlit session state:

- `st.session_state["model_config"]`:
  `provider`, `model_name`, `version`, `api_status`, `prompt`
- `st.session_state["test_config"]`:
  `tests`, `strictness`, `threshold`
- Backend should store actual evaluation output in:
  `st.session_state["evaluation_results"]`
- Optional version comparison payload:
  `st.session_state["comparison_data"]`

Expected evaluation result shape:

```python
{
    "is_sample": False,
    "model_name": "model identifier",
    "overall_score": 84,
    "status": "PASS",
    "categories": [
        {
            "name": "Hallucination",
            "score": 90,
            "status": "PASS",
            "details": "Evidence and explanation"
        }
    ]
}
```

This ZIP does **not** include a real model evaluator, API keys, database, or authentication. The dashboard and default results are sample/demo data. Connect the backend before claiming that evaluations are real.

## Run checks

```powershell
python -m compileall frontend
python -m streamlit --version
```
