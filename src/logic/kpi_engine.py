def analyze_kpis(df):
    kpis = {}
    if "Status" in df.columns:
        kpis["Total Tickets"] = len(df)
        kpis["Open Tickets"] = df["Status"].str.lower().eq("open").sum()
        kpis["Closed Tickets"] = df["Status"].str.lower().eq("closed").sum()
    if "SLA Met" in df.columns:
        kpis["SLA Compliance %"] = round(df["SLA Met"].mean() * 100, 2)
    return kpis
