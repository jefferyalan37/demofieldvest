import streamlit as st
st.set_page_config(page_title="Fieldvest Demo", layout="wide")  # ← ONLY this call

from components.onboarding import run_onboarding
from components.browse import show_browse
from components.dashboard import show_dashboard

def main():
    st.sidebar.title("Navigation")

    # Initialize flag
    if "onboarding_complete" not in st.session_state:
        st.session_state.onboarding_complete = False

    # If not onboarded yet, run the wizard
    if not st.session_state.onboarding_complete:
        run_onboarding()
        return

    # Once onboarded, show sidebar nav
    choice = st.sidebar.radio("Go to", ("Browse Investments", "Dashboard"))
    if choice == "Browse Investments":
        show_browse()
    else:
        show_dashboard()

if __name__ == "__main__":
    main()
