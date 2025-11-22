import pandas as pd
import streamlit as st

def load_file(uploaded_file):
    try:
        if uploaded_file.name.endswith(".csv"):
            return pd.read_csv(uploaded_file), "csv"
        elif uploaded_file.name.endswith(".xlsx"):
            return pd.read_excel(uploaded_file, engine="openpyxl"), "excel"
        else:
            raise ValueError("Unsupported file format.")
    except Exception as e:
        st.error(f"File loading error: {e}")
        return pd.DataFrame(), None
