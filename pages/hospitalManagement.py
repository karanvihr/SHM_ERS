import streamlit as st 


with st.container(): 
    if st.button("Back"):
        st.switch_page("pages/home.py")