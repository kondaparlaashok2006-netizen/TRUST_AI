import streamlit as st

COLORS = {
    "background": "#2A2A2A", "sidebar": "#222222",
    "surface": "#333333", "surface_light": "#404040",
    "primary": "#E10600", "primary_hover": "#B80500",
    "secondary": "#C0C0C0", "text": "#F5F5F5",
    "muted": "#B0B0B0", "border": "#555555",
}

def apply_custom_styles():
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
    html, body, .stApp, [data-testid="stAppViewContainer"],
    h1,h2,h3,h4,h5,h6,p,label,input,textarea,button {
        font-family:'Josefin Sans',sans-serif !important;
    }
    .stApp {background:#2A2A2A;color:#F5F5F5;}
    .block-container {max-width:1450px;padding-top:2rem;padding-bottom:2rem;}
    [data-testid="stSidebar"] {background:#222222;border-right:1px solid #555555;}
    [data-testid="stMetric"] {background:#333333;border:1px solid #555555;border-radius:12px;padding:18px;}
    [data-testid="stMetricLabel"] {color:#C0C0C0 !important;}
    [data-testid="stMetricValue"] {color:#FFFFFF !important;font-weight:700;}
    .stButton>button {background:#E10600;color:#FFFFFF;border:1px solid #E10600;border-radius:9px;min-height:42px;font-weight:700;}
    .stButton>button:hover {background:#B80500;border-color:#B80500;color:#FFFFFF;}
    .stButton>button[kind="secondary"] {background:#333333;color:#C0C0C0;border-color:#555555;}
    .stButton>button[kind="secondary"]:hover {background:#404040;border-color:#E10600;color:#FFFFFF;}
    .trust-card {background:#333333;border:1px solid #555555;border-radius:12px;padding:18px;margin-bottom:12px;}
    .page-title {color:#F5F5F5;font-size:36px;font-weight:800;margin-bottom:4px;}
    .page-subtitle {color:#C0C0C0;font-size:15px;}
    .page-accent {width:65px;height:4px;background:#E10600;border-radius:5px;margin-top:12px;}
    hr {border-color:#555555;}
    </style>
    """, unsafe_allow_html=True)

def render_page_header(title, subtitle):
    st.markdown(f'<div style="margin-bottom:25px"><h1 class="page-title">{title}</h1><p class="page-subtitle">{subtitle}</p><div class="page-accent"></div></div>', unsafe_allow_html=True)

def render_brand():
    st.markdown("""
    <div style="display:flex;align-items:center;gap:12px">
      <div style="background:#E10600;color:white;width:42px;height:42px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:23px;font-weight:800">T</div>
      <div><div style="color:#E10600;font-size:25px;font-weight:800">TRUST-AI</div>
      <div style="color:#C0C0C0;font-size:10px;letter-spacing:1px">RESPONSIBLE AI PLATFORM</div></div>
    </div>
    """, unsafe_allow_html=True)
