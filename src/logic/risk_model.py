def calculate_risk_scores(df, mappings):
    high_priority = df[mappings["Priority"]].str.lower().eq("high").sum()
    return {
        "High Priority Count": high_priority,
        "High Priority %": round(100 * high_priority / len(df), 2)
    }