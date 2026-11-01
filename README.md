<div align="center">

# 🛡️ TRUST-AI

### Don't Just Generate AI. Evaluate It.

**A Responsible AI Output Evaluation Dashboard**

Understand AI outputs. Examine their weaknesses. Make trust more transparent.

<br>

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Responsible AI](https://img.shields.io/badge/Responsible-AI-6A5ACD?style=for-the-badge)
![Project Status](https://img.shields.io/badge/Status-Frontend%20Starter-orange?style=for-the-badge)

<br>

**TRUST-AI — Evaluate Intelligence. Build Trust.**

</div>

---

## 🌟 What is TRUST-AI?

AI-generated responses can sound convincing without being correct, reliable, or appropriate.

TRUST-AI is designed to help users evaluate AI-generated outputs through a structured and transparent evaluation workflow.

Instead of looking only at what an AI model generates, TRUST-AI focuses on understanding how its outputs perform under defined evaluation tests.

The platform provides an interactive dashboard for configuring models, selecting tests, examining evaluation results, comparing model versions, and exporting reports.

> 💡 **Our idea:** AI should not only generate answers. Its outputs should also be evaluated.

---

## 🎯 Why TRUST-AI?

| ⚠️ Challenge                                   | 💡 TRUST-AI Approach                             |
| ---------------------------------------------- | ------------------------------------------------ |
| AI responses may contain incorrect information | Support structured output evaluation             |
| A single score may hide important weaknesses   | Present category-level evaluation results        |
| Model updates may change output behavior       | Provide a version-comparison interface           |
| Evaluation results can be difficult to share   | Support JSON, CSV, and PDF reports               |
| AI assessment can feel like a black box        | Present results through an interactive dashboard |

**Our goal is to make AI evaluation easier to understand—not to claim that any model is automatically trustworthy.**

---

## ✨ Features

### 📊 Interactive Evaluation Dashboard

Explore evaluation metrics and result summaries through a clean dashboard.

### ⚙️ Model Configuration

Configure the AI provider, model name, version, and prompt.

### 🧪 Test Configuration

Select evaluation tests and configure evaluation parameters.

### 🔍 Evaluation Results

Examine overall scores, category-level assessments, and supporting explanations.

### 🔄 Model Version Comparison

Explore an interface for comparing results across model versions.

### 📄 Report Generation

Download evaluation reports in JSON, CSV, and PDF formats.

### 🎨 Modern Interface

A distinctive charcoal, silver, and signal-red visual theme with Josefin Sans typography.

---

## 🖥️ Dashboard Preview

<div align="center">

<!-- Add your actual dashboard screenshot here -->

**TRUST-AI Evaluation Dashboard**

*Replace this section with a screenshot of your running dashboard.*

</div>

---

# 🚀 Installation & Setup

Get TRUST-AI running on your computer in a few minutes.

## 📋 Prerequisites

Before installing, make sure you have:

| Requirement                       | Purpose              |
| --------------------------------- | -------------------- |
| Python 3.12 or compatible version | Run the application  |
| Git                               | Clone the repository |
| PowerShell / Terminal             | Execute commands     |
| Internet connection               | Install dependencies |

Check your Python installation:

```bash
python --version
```

Check Git:

```bash
git --version
```

If Python or Git is not installed, install them before continuing.

---

## 📥 Step 1 — Get the Project

### Option A: Clone using Git

Recommended for developers and contributors.

```bash
git clone https://github.com/kondaparlaashok2006-netizen/TRUST_AI.git
```

Move into the project directory:

```bash
cd TRUST_AI
```

### Option B: Download as ZIP

Prefer not to use Git?

1. Open the TRUST-AI GitHub repository.
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Extract the ZIP file.
5. Open a terminal inside the extracted project folder.

Both options provide the project source code.

---

## 🪟 Step 2 — Windows Installation

Open PowerShell inside the TRUST-AI project folder.

### Create a virtual environment

If you already have a `.venv` folder, skip this command.

```powershell
py -3.12 -m venv .venv
```

### Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment again:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Launch TRUST-AI

```powershell
python -m streamlit run frontend\dashboard.py
```

🎉 **That's it!** Streamlit should open the TRUST-AI dashboard in your browser.

If it does not open automatically, visit:

```text
http://localhost:8501
```

### ⚡ Quick Launch

On Windows, you can also use:

```powershell
.\run.bat
```

---

## 🐧 Step 3 — Linux / macOS Installation

Open your terminal inside the project directory.

### Create a virtual environment

```bash
python3 -m venv .venv
```

### Activate the environment

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Run the dashboard

```bash
python -m streamlit run frontend/dashboard.py
```

Open the dashboard at:

```text
http://localhost:8501
```

---

## 🧰 Troubleshooting

### ❌ Python is not recognized

Check whether Python is installed:

```powershell
py --version
```

If the command is unavailable, install Python and ensure it is accessible from your terminal.

### ❌ Streamlit is not installed

Run:

```powershell
python -m pip install -r requirements.txt
```

Then:

```powershell
python -m streamlit run frontend\dashboard.py
```

### ❌ Virtual environment activation fails

For Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

### ❌ Port 8501 is already in use

Start Streamlit on another port:

```powershell
python -m streamlit run frontend\dashboard.py --server.port 8502
```

Open:

```text
http://localhost:8502
```

---

## 🏗️ Project Structure

```text
TRUST-AI/
│
├── frontend/
│   └── dashboard.py
│
├── requirements.txt
├── run.bat
├── README.md
└── .gitignore
```

The current structure represents the frontend starter. Backend modules may be added as the evaluation system evolves.

---

## 🔌 Backend Integration

The frontend uses Streamlit session state to exchange configuration and evaluation results.

| Session State        | Purpose                                         |
| -------------------- | ----------------------------------------------- |
| `model_config`       | Model provider, model name, version, and prompt |
| `test_config`        | Selected tests, strictness, and threshold       |
| `evaluation_results` | Actual evaluation output                        |
| `comparison_data`    | Optional version comparison information         |

The backend should populate:

```python
st.session_state["evaluation_results"]
```

Expected result structure:

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

The values above are illustrative examples, not actual evaluation results.

---

## ⚠️ Project Status

**Current stage: Frontend Starter**

The current version provides the dashboard interface and integration contract.

The starter includes illustrative sample metrics and default results.

It does **not** include a complete real model evaluator, API credentials, database, or authentication system.

A connected backend is required before presenting dashboard results as actual AI evaluations.

---

## 🔐 Security

* Never commit API keys or credentials.
* Keep `.env` files out of version control.
* Use environment variables for secrets.
* Do not publish private credentials in screenshots or reports.
* Clearly distinguish sample data from real evaluation results.

---

## 👥 Team

**Developed at SRK Institute of Technology**

Built with the goal of making AI evaluation more transparent, understandable, and responsible.

---

## 💬 Our Vision

> "The future of AI is not only about what models can generate. It is about whether people can trust what they generate."

<div align="center">

### 🛡️ TRUST-AI

**Evaluate Intelligence. Build Trust.**

</div>
