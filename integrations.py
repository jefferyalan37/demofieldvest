import streamlit as st

def calculate_tax_savings(amount: float, income_range: str) -> float:
    """
    Returns an estimate of first-year tax savings on an oil & gas investment.
    - amount: investment amount in $
    - income_range: one of the dropdown labels from onboarding
    """
    # Map the income bracket to a marginal tax rate
    bracket_rates = {
        "$50k - $100k": 0.22,
        "$100k - $250k": 0.24,
        "$250k - $500k": 0.32,
        "$500k+": 0.35
    }
    rate = bracket_rates.get(income_range, 0.24)
    # Oil & gas intangible drilling costs are ~80% deductible in year 1
    deduction_pct = 0.80
    return amount * deduction_pct * rate

def link_bank(user_id: str) -> bool:
    """
    Mock bank-link flow; in real life you'd call Plaid or similar.
    """
    # simulate a successful link
    st.session_state.bank_linked = True
    return True

def persist_reservation(user_id: str, project_id: str, units: int):
    """
    Save the user's reservation in session state.
    """
    if "reservations" not in st.session_state:
        st.session_state.reservations = []
    st.session_state.reservations.append({
        "user_id": user_id,
        "project_id": project_id,
        "units": units
    })
    return True

