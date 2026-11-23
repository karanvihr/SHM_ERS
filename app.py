import streamlit as st
st.set_page_config(
    page_title = "SHM ERS",
    layout = "wide"
)




# Sidebar title
st.sidebar.title("SHM ERS")
st.sidebar.caption("Hospital Management System")


# Sidebar heading
# st.logo("logo.png", size="large")


# Default navigation
home = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠",
    default=True
)

hospital = st.Page(
    "pages/hospitalManagement.py",
    title="Hospital",
    icon="🏥"

)

emergency = st.Page(
    "pages/emergencyResponse.py",
    title="Emergency",
    icon="🚨"
)

signup = st.Page(
    "pages/signup.py",
    title="Login",
    icon="👤"

)

pg = st.navigation([home, hospital, emergency, signup])

pg.run()