import streamlit as st
from ui.layout import render_header
from data.ingestion import load_data
from metrics.kpi_engine import compute_kpis
from metrics.risk_model import score_risks
from metrics.insights_engine import generate_insights

st.set_page_config(page_title="CX Analytics Tool", layout="wide")
render_header()

uploaded_file = st.file_uploader("Upload CX data", type=["csv", "xlsx"])
if uploaded_file:
    df, meta = load_data(uploaded_file)
    st.subheader("Preview of Uploaded Data")
    st.dataframe(df.head())

    kpis = compute_kpis(df)
    risks = score_risks(df)
    insights = generate_insights(df)

    st.subheader("📊 Key Metrics")
    st.json(kpis)

    st.subheader("⚠️ Risk Scoring")
    st.json(risks)

    st.subheader("🔍 Insights")
    for item in insights:
        st.markdown(f"- {item}")