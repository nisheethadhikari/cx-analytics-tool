def calculate_risk_score(df):
    if 'Priority' not in df:
        return {"High Priority Count": 0, "High Priority %": 0.0}
    high_priority = df[df['Priority'].str.lower() == 'high']
    count = len(high_priority)
    percent = (count / len(df)) * 100 if len(df) > 0 else 0
    return {"High Priority Count": count, "High Priority %": round(percent, 2)}