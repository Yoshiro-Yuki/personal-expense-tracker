import gspread
from datetime import datetime, timezone, date
from zoneinfo import ZoneInfo
import streamlit as st

START_DATE = date(2026, 10, 28)

def day_diff(curr: date) -> int:
    return (curr - START_DATE).days

def save_deposit(amount: float, category: str) -> dict:
    now = datetime.now(ZoneInfo("Asia/Manila"))
    gap = day_diff(now.date())

    gc = gspread.service_account_from_dict(dict(st.secrets["gcp_service_account"]))
    wks = gc.open_by_url(st.secrets["gcp_url"]).worksheet("Daily Tracker Expenses")
    wks.append_row([now.timestamp(), now.date().isoformat(), gap, category, amount])

    return {"status": "ok", "amount": amount, "category": category}
