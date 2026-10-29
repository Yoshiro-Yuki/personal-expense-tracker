import gspread
from datetime import datetime, timezone, date
import streamlit as st

START_DATE = date(2026, 10, 28)
KEY_FILE = dict(st.secrets["gcp_service_account"])
SHEET_URL = st.secrets["gcp_url"]

def day_diff(curr: date) -> int:
    return (curr - START_DATE).days

def save_deposit(amount: float, category: str) -> dict:
    now = datetime.now(timezone.utc)
    gap = day_diff(now.date())

    gc = gspread.service_account(filename=KEY_FILE)
    wks = gc.open_by_url(SHEET_URL).worksheet("Daily Tracker Expenses")
    wks.append_row([now.timestamp(), now.date().isoformat(), gap, category, amount])

    return {"status": "ok", "amount": amount, "category": category}

if __name__ == "__main__":
    print(save_deposit(2000, "test"))
