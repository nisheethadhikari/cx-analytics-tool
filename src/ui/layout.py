import streamlit as st
import altair as alt
import pandas as pd

def render_main_layout(df, kpi_results, risks):
    st.subheader("📈 Trend Overview")
    if "Date" in df.columns and "Status" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
        trend = df.groupby(df["Date"].dt.to_period("M")).size().reset_index(name='Tickets')
        trend["Date"] = trend["Date"].astype(str)
        chart = alt.Chart(trend).mark_line().encode(x="Date", y="Tickets")
        st.altair_chart(chart, use_container_width=True)

    st.subheader("🔍 Insights")
    st.write("Based on current risk scoring and SLA trends, consider reviewing high-risk accounts for QBR acceleration.")
