import streamlit as st

def manual_column_mapper(df, expected_fields):
    st.info("Auto-detection failed. Please map columns manually.")
    mappings = {}
    for field in expected_fields:
        column = st.selectbox(f"Map for '{field}'", df.columns, key=field)
        mappings[field] = column
    return mappings
