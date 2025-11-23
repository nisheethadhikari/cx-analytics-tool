def calculate_kpis(df):
    total = len(df)
    open_tickets = len(df[df['Status'].str.lower() == 'open']) if 'Status' in df else 0
    closed_tickets = len(df[df['Status'].str.lower() == 'closed']) if 'Status' in df else 0
    return {
        "Total Tickets": total,
        "Open Tickets": open_tickets,
        "Closed Tickets": closed_tickets
    }