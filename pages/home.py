import streamlit as st

st.title("Management & Response System")

hero = st.container()

with hero:
    st.space()
    st.space()
    st.write("Welcome to SHM_ERS")
    st.write("Smart Hospital Management and Emergency Response System")
    st.write("Manage your system easily and efficiently.")
    st.space()
    st.space()


content = st.container()

with content:
    st.header("Our Features")
    if st.button("Hospital Management"):
        st.switch_page("pages/hospitalManagement.py")
    if st.button("Emergency Response"):
        st.switch_page("pages/emergencyResponse.py")