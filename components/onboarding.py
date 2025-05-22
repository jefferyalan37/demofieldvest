# components/onboarding.py

import streamlit as st
from integrations import calculate_tax_savings

def run_onboarding():
    # Initialize step
    if "onboarding_step" not in st.session_state:
        st.session_state.onboarding_step = 1

    step = st.session_state.onboarding_step

    # STEP 1: Welcome
    if step == 1:
        st.title("Own more. Owe less.")
        st.write("Welcome to Fieldvest—discover tax-advantaged oil & gas investments.")
        if st.button("Get Started"):
            st.session_state.onboarding_step = 2
        return

    # STEP 2: Quick Profile
    if step == 2:
        st.header("Quick Profile")
        with st.form("profile_form"):
            income = st.selectbox(
                "Income range",
                ["$50k - $100k", "$100k - $250k", "$250k - $500k", "$500k+"]
            )
            state = st.selectbox(
                "State of residence",
                ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL",
                 "IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT",
                 "NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI",
                 "SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
            )
            accredited = st.radio(
                "Accredited investor?",
                ("Yes", "No")
            )
            submitted = st.form_submit_button("Next")
        if submitted:
            st.session_state.profile = {
                "income": income,
                "state": state,
                "accredited": accredited == "Yes"
            }
            st.session_state.onboarding_step = 3
        return

    # STEP 3: Tax Savings Estimate
    if step == 3:
        profile = st.session_state.profile
        st.header("Estimate Your Tax Savings")
        st.write(
            f"For a $100,000 investment, your estimated first-year tax savings are:"
        )
        tax_savings = calculate_tax_savings(
            amount=100_000,
            income_range=profile["income"]
        )
        st.metric(label="Tax Savings", value=f"${tax_savings:,.0f}")
        if st.button("View Investments"):
            st.session_state.onboarding_complete = True
        return
