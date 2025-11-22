def generate_insights(kpis, risks):
    insights = []
    if kpis.get("Open Tickets", 0) > 5000:
        insights.append("High open ticket volume; monitor backlog.")
    if risks.get("High Priority %", 0) > 15:
        insights.append("High risk ticket ratio exceeds safe threshold.")
    return insights