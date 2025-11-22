def calculate_risk_scores(df):
    risk_scores = {}
    if "Priority" in df.columns:
        high_risk = df[df["Priority"].str.lower() == "high"]
        risk_scores["High Priority Count"] = len(high_risk)
        risk_scores["High Priority %"] = round(len(high_risk) / len(df) * 100, 2) if len(df) else 0
    return risk_scores
