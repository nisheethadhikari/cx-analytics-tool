import streamlit as st
import altair as alt
import pandas as pd

def render_main_layout(df, kpi_results, risks, insights):
    st.subheader("📌 Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Tickets", f"{kpi_results.get('Total Tickets', 0):,}")
    col2.metric("Open Tickets", f"{kpi_results.get('Open Tickets', 0):,}")
    col3.metric("Closed Tickets", f"{kpi_results.get('Closed Tickets', 0):,}")
    if "SLA Compliance %" in kpi_results:
        st.metric("SLA Compliance %", f"{kpi_results['SLA Compliance %']}%")

    st.subheader("🚨 Risk Scoring")
    col4, col5 = st.columns(2)
    col4.metric("High Priority Count", f"{risks.get('High Priority Count', 0):,}")
    col5.metric("High Priority %", f"{risks.get('High Priority %', 0):.2f}%")

    if insights:
        st.subheader("💡 Insights")
        for tip in insights:
            st.write(f"- {tip}")

    if "Date" in df.columns:
        st.subheader("📈 Trend Overview")
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df.dropna(subset=["Date"], inplace=True)
        monthly = df.groupby(df["Date"].dt.to_period("M")).size().reset_index(name="Tickets")
        monthly["Date"] = monthly["Date"].astype(str)
        chart = alt.Chart(monthly).mark_line().encode(x="Date", y="Tickets")
        st.altair_chart(chart, use_container_width=True)
