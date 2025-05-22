# components/browse.py

import streamlit as st
from data import get_projects
from integrations import calculate_tax_savings, link_bank, persist_reservation

def show_browse():
    st.title("Browse Projects")
    profile = st.session_state.profile
    income_range = profile["income"]

    projects = get_projects()
    for proj in projects:
        # Card-like layout
        cols = st.columns([1, 2])
        with cols[0]:
            st.image(proj["image_url"], use_column_width=True)
        with cols[1]:
            st.subheader(proj["name"])
            st.write(f"**Target IRR:** {proj['target_irr']*100:.1f}%")
            st.write(f"**Minimum Investment:** ${proj['min_investment']:,.0f}")
            # Tax savings per $100K
            tax_sav = calculate_tax_savings(100_000, income_range)
            st.write(f"**Est. Tax Savings per $100K:** ${tax_sav:,.0f}")

            # Reserve flow
            units = st.number_input(
                "Units to Reserve",
                min_value=1,
                value=1,
                step=1,
                key=f"{proj['id']}_units"
            )
            if st.button(
                "Reserve Units",
                key=f"{proj['id']}_reserve"
            ):
                # Simulate bank link & persistence
                if not st.session_state.get("bank_linked", False):
                    link_bank(user_id="demo_user")
                persist_reservation(
                    user_id="demo_user",
                    project_id=proj["id"],
                    units=units
                )
                st.success(f"Reserved {units} unit(s) of **{proj['name']}**")

        st.markdown("---")

