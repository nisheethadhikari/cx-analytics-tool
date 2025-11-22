import streamlit as st
from data.ingestion import load_file
from data.mapping_ui import manual_column_mapper
from logic.kpi_engine import compute_kpis
from logic.risk_model import calculate_risk_scores
from logic.insights import generate_insights

def render_main_ui():
    st.title("CX Analytics Tool")
    uploaded_file = st.file_uploader("Upload Data", type=["csv", "xlsx"])

    if uploaded_file:
        df, _ = load_file(uploaded_file)
        if df.empty:
            st.error("Unable to read file or file is empty.")
            return

        expected_fields = ["Status", "Priority"]
        mappings = manual_column_mapper(df, expected_fields)

        st.subheader("Preview of Uploaded Data")
        st.dataframe(df.head())

        kpis = compute_kpis(df, mappings)
        st.subheader("📌 Key Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Tickets", f"{kpis.get('Total Tickets', 0):,}")
        col2.metric("Open Tickets", f"{kpis.get('Open Tickets', 0):,}")
        col3.metric("Closed Tickets", f"{kpis.get('Closed Tickets', 0):,}")

        risks = calculate_risk_scores(df, mappings)
        st.subheader("⚠️ Risk Scoring")
        col4, col5 = st.columns(2)
        col4.metric("High Priority Count", f"{risks.get('High Priority Count', 0):,}")
        col5.metric("High Priority %", f"{risks.get('High Priority %', 0):.1f}")

        st.subheader("📈 Trend Overview")
        st.markdown("_(Placeholder for time series / trend plots)_")

        st.subheader("🔍 Insights")
        for insight in generate_insights(kpis, risks):
            st.write(f"- {insight}")