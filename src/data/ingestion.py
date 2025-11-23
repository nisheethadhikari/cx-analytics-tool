import pandas as pd

def load_data(uploaded_file):
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file, sheet_name=0)
    else:
        raise ValueError("Unsupported file format")

    meta = {
        "rows": len(df),
        "columns": list(df.columns),
        "missing_pct": df.isna().mean().to_dict()
    }
    return df, meta