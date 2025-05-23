import streamlit as st

from components.onboarding import run_onboarding
from components.browse import show_browse
from components.dashboard import show_dashboard
import streamlit as st

# ——— Inject Bodoni Moda + custom CSS ———
st.markdown(
    """
    <style>
      /* 1. Import Bodoni Moda (400 & 700) */
      @import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:wght@400;700&display=swap');

      /* 2. Apply it globally */
      html, body, [class*="css"] {
        font-family: 'Bodoni Moda', serif !important;
      }

      /* 3. Make all headings regular weight (400) */
      h1, h2, h3, h4, h5, h6 {
        font-weight: 400 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# Now your normal page config…
st.set_page_config(page_title="Fieldvest Demo", layout="wide")

# …the rest of your app.py follows


def main():
    st.set_page_config(page_title="Fieldvest Demo", layout="wide")
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
