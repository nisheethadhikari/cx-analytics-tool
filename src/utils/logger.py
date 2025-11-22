from datetime import datetime

def log_event(message):
    print(f"[{datetime.now().isoformat()}] {message}")
