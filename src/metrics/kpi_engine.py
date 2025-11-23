def compute_kpis(df):
    created_col = next((col for col in df.columns if "created" in col.lower()), None)
    status_col = next((col for col in df.columns if "status" in col.lower()), None)

    if not created_col or not status_col:
        return {"error": "Required fields not found"}

    total = len(df)
    open_ = len(df[df[status_col].str.lower() == "open"])
    closed = len(df[df[status_col].str.lower().isin(["closed", "resolved"])])

    return {
        "Total Tickets": total,
        "Open Tickets": open_,
        "Closed Tickets": closed
    }