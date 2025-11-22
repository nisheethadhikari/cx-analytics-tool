import streamlit as st
from auth.login import login_screen
from ui.layout import render_main_layout
from logic.kpi_engine import analyze_kpis
from logic.risk_model import calculate_risk_scores
from data.parser import load_dataset
from utils.logger import log_event

# Step 1: Authenticate user
if not login_screen():
    st.stop()

# Step 2: Upload data
st.title("📊 CX Analytics Tool")
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Step 3: Load and parse dataset
    df = load_dataset(uploaded_file)
    st.subheader("Preview of Uploaded Data")
    st.dataframe(df.head())

    # Step 4: Analyze KPIs
    kpi_results = analyze_kpis(df)
    st.subheader("Key Metrics")
    st.json(kpi_results)

    # Step 5: Risk Calculation
    risks = calculate_risk_scores(df)
    st.subheader("Risk Scoring")
    st.json(risks)

    # Step 6: Log user activity
    log_event("Data analyzed and risk scores generated.")

    # Step 7: Render the full layout (charts, actions, etc.)
    render_main_layout(df, kpi_results, risks)
else:
    st.info("Please upload a file to begin analysis.")
