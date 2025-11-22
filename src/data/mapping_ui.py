import streamlit as st

def manual_column_mapper(df, expected_fields):
    mappings = {}
    for field in expected_fields:
        mappings[field] = st.selectbox(f"Map column for: {field}", df.columns, key=field)
    return mappings