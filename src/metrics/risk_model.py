def score_risks(df):
    priority_col = next((col for col in df.columns if "priority" in col.lower()), None)
    if not priority_col:
        return {"High Priority Count": 0, "High Priority %": 0.0}

    high_priority = df[df[priority_col].str.lower() == "high"]
    count = len(high_priority)
    percentage = round((count / len(df)) * 100, 2) if len(df) > 0 else 0

    return {
        "High Priority Count": count,
        "High Priority %": percentage
    }