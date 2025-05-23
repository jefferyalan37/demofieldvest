import streamlit as st
st.set_page_config(page_title="Fieldvest Demo", layout="wide")  # ← ONLY this call

# now all your other imports
from components.onboarding import run_onboarding
from components.browse import show_browse
from components.dashboard import show_dashboard

def main():
    st.sidebar.title("Navigation")
    # … rest of your logic …

if __name__ == "__main__":
    main()
