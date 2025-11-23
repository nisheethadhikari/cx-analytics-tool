import streamlit as st
from ui.layout import render_layout
from utils.file_loader import load_file
from metrics.kpi_engine import calculate_kpis
from metrics.risk_model import calculate_risk_score

st.set_page_config(page_title="CX Analytics Tool", layout="wide")
render_layout()

uploaded_file = st.file_uploader("Upload your data file", type=["csv", "xlsx"])

if uploaded_file:
    df = load_file(uploaded_file)
    st.subheader("📄 Preview of Uploaded Data")
    st.dataframe(df.head())

    kpis = calculate_kpis(df)
    risk = calculate_risk_score(df)

    st.subheader("📊 Key Metrics")
    st.json(kpis)

    st.subheader("⚠️ Risk Scoring")
    st.json(risk)

    st.subheader("📈 Trend Overview")
    st.caption("(Placeholder for time series / trend plots)")

    st.subheader("🔍 Insights")
    st.markdown("Based on current scoring and trends, take proactive steps.")