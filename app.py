# app.py
import streamlit as st

# ← THIS MUST BE THE VERY FIRST Streamlit COMMAND IN YOUR SCRIPT
st.set_page_config(page_title="Fieldvest Demo", layout="wide")

# now it’s safe to import your components
from components.onboarding import run_onboarding
from components.browse import show_browse
from components.dashboard import show_dashboard

def main():
    st.sidebar.title("Navigation")

    # initialize your onboarding flag
    if "onboarding_complete" not in st.session_state:
        st.session_state.onboarding_complete = False

    # run onboarding flow if needed
    if not st.session_state.onboarding_complete:
        run_onboarding()
        return

    # once onboarded, show the nav
    choice = st.sidebar.radio("Go to", ("Browse Investments", "Dashboard"))
    if choice == "Browse Investments":
        show_browse()
    else:
        show_dashboard()

if __name__ == "__main__":
    main()
