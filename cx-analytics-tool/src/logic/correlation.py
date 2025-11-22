import pandas as pd

def compute_correlation(df, col1, col2):
    if col1 in df.columns and col2 in df.columns:
        return df[[col1, col2]].corr().iloc[0, 1]
    return None
