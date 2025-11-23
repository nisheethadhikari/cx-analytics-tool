import pandas as pd

def compute_correlation(df, target_col, features=None):
    df_numeric = df.select_dtypes(include="number")
    if features:
        df_numeric = df_numeric[features + [target_col]]
    if target_col not in df_numeric.columns:
        return {}
    return df_numeric.corr()[target_col].drop(target_col).to_dict()