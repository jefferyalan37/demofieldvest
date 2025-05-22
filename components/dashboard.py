# components/dashboard.py

import streamlit as st
import pandas as pd
from data import get_projects
from integrations import calculate_tax_savings

def show_dashboard():
    st.title("Your Dashboard")

    # Grab reservations (made via show_browse)
    reservations = st.session_state.get("reservations", [])
    if not reservations:
        st.info("You have no active investments yet. Head over to Browse to reserve units.")
        return

    # Build a lookup of project data
    projects = {p["id"]: p for p in get_projects()}

    # Prepare portfolio summary
    rows = []
    total_invested = 0
    total_tax_savings = 0
    for r in reservations:
        proj = projects.get(r["project_id"], {})
        invested = proj.get("min_investment", 0) * r["units"]
        tax_sav = calculate_tax_savings(invested, st.session_state.profile["income"])
        rows.append({
            "Project": proj.get("name", r["project_id"]),
            "Units": r["units"],
            "Invested ($)": invested,
            "Est. Tax Savings ($)": int(tax_sav),
        })
        total_invested += invested
        total_tax_savings += tax_sav

    # Summary metrics
    st.subheader("Portfolio Summary")
    col1, col2 = st.columns(2)
    col1.metric("Total Invested", f"${total_invested:,.0f}")
    col2.metric("Total Tax Savings", f"${total_tax_savings:,.0f}")

    # Show table of individual positions
    st.subheader("Positions")
    df = pd.DataFrame(rows)
    st.table(df)

    # Simulate monthly cashflow chart
    st.subheader("Projected Monthly Cashflow")
    # Simple model: each position yields (invested * IRR)/12 per month
    monthly = {}
    for r in reservations:
        proj = projects[r["project_id"]]
        monthly_yield = (proj["target_irr"] * proj["min_investment"] * r["units"]) / 12
        for m in range(1, 13):
            monthly[f"Month {m}"] = monthly.get(f"Month {m}", 0) + monthly_yield
    cashflow_df = pd.DataFrame({
        "Month": list(monthly.keys()),
        "Cashflow ($)": list(monthly.values())
    }).set_index("Month")
    st.bar_chart(cashflow_df)

    # Placeholder for tax forms
    st.subheader("Year-End Tax Forms")
    for r in reservations:
        proj = projects[r["project_id"]]
        st.write(f"- {proj['name']}: [Download K-1]()")

