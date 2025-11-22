def compute_kpis(df, mappings):
    return {
        "Total Tickets": len(df),
        "Open Tickets": df[mappings["Status"]].str.lower().eq("open").sum(),
        "Closed Tickets": df[mappings["Status"]].str.lower().eq("closed").sum(),
    }