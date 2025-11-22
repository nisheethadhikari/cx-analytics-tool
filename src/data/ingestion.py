import pandas as pd

def load_file(uploaded_file):
    try:
        if uploaded_file.name.endswith(".csv"):
            return pd.read_csv(uploaded_file), "csv"
        elif uploaded_file.name.endswith(".xlsx"):
            return pd.read_excel(uploaded_file), "excel"
        else:
            raise ValueError("Unsupported file format.")
    except Exception:
        return pd.DataFrame(), None