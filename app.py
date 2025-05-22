import streamlit as st

# Import your components
from components.onboarding import (
    # since onboarding reruns internally, we only need to call it
    )
from components.browse import show_browse
from components.dashboard import show_dashboard

def main():
    st.set_page_config(page_title="Fieldvest Demo", layout="wide")
    st.sidebar.title("Navigation")

    # Initialize session flags
    if "onboarding_complete" not in st.session_state:
        st.session_state.onboarding_complete = False

    # Sidebar navigation
    if st.session_state.onboarding_complete:
        choice = st.sidebar.radio(
            "Go to",
            ("Browse Investments", "Dashboard"),
            index=0
        )
    else:
        choice = None

    # --- Onboarding (3-step) ---
    if not st.session_state.onboarding_complete:
        # import & run the onboarding flow
        from components.onboarding import run_onboarding
        run_onboarding()
        return

    # --- Post-Onboarding Flows ---
    if choice == "Browse Investments":
        show_browse()
    else:  # Dashboard
        show_dashboard()


if __name__ == "__main__":
    main()

