def generate_insights(df):
    insights = []
    if "SLA_Breached__c" in df.columns:
        breached = df["SLA_Breached__c"].sum()
        if breached > 0:
            insights.append(f"{breached} tickets breached SLA.")
    if "Escalated" in df.columns and df["Escalated"].sum() > 0:
        insights.append("Multiple escalations detected.")
    if len(insights) == 0:
        insights.append("No major issues found.")
    return insights