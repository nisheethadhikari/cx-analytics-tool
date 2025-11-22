def generate_insights(kpis, risks):
    insights = []
    if kpis.get("SLA Compliance %", 100) < 80:
        insights.append("SLA compliance is below acceptable threshold.")
    if risks.get("High Priority %", 0) > 15:
        insights.append("High concentration of high-priority tickets.")
    if kpis.get("Open Tickets", 0) > 5000:
        insights.append("Backlog volume is increasing; consider workforce balancing.")
    return insights
