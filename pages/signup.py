import re 
import streamlit as st
from database.auth import login_user
from database.auth import register_user
from models.patient import Patient


st.set_page_config(
    page_title="SHM ERS -signup",
    layout = "centered"
)


# create session_variables once
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None




st.title("SHM ERS")
st.write("the Smart Hospital Management and Emergency Response System.")

# creating login,signup tabs
login_tab,signup_tab = st.tabs(["🔐 Login","📝 Sign Up"])

with login_tab:

    st.subheader("Login to your account")
    if st.session_state.user != None:
        st.write(f"Welcome back! {st.session_state.user["full_name"]}") 

    with st.form("login_form"):

        email = st.text_input(
            "Email",
            key="login_email"
            )
        
        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
            )

        submitted = st.form_submit_button(
            "Login",
            use_container_width=True
            )

        if submitted:
            email = email.strip().lower()

            if not email or not password:
                st.error("Please enter your email and password.")

            else:
                success,message,user = login_user(email,password)

                if success:
                    st.session_state.logged_in = True
                    st.session_state.user = user

                    st.success(message)
                    st.write(f"welcome, {user["full_name"]}!")
                    st.write(f"your role: {user["role"]}")

                else:
                    st.error(message)




with signup_tab:

    with st.form("signup_form"):
    
        full_name = st.text_input("Full Name")
        age = st.text_input("Age")
        phone_no = st.text_input("Phone no.")
        email = st.text_input("Email Adderess")
        address = st.text_input("Address")

        role = st.selectbox(
        "Register As",
        ["Select","Patient","Doctor","Nurse"]
        ) 




        password = st.text_input(
            "Password",
            type= "password")

        confirm_password = st.text_input(
            "Confirm password",
            type="password")

        submitted = st.form_submit_button(
            "Create Account",
            use_container_width=True
        )

        if submitted:
            full_name = full_name.strip()
            email = email.strip().lower()

            if not full_name or not email or not password or not age or not phone_no or not address :
                st.error("Please fill in all required fields.")

            elif not isinstance(phone_no,int) or len(str(phone_no)!=10):
                st.error("Please enter valid phone number")

            elif not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+",email):
                st.error("Please enter a valid email.")

            elif len(password)<8:
                st.error("Password must contain atleast 8 characters.")

            elif password != confirm_password:
                st.error("Passwords do not match.")

            else:
                success,message = register_user(
                    full_name,
                    email,
                    password,
                    role
                    )

                if success:
                    st.success(message)
                    st.info("you can now go to the login page.")

                else:
                    st.error(message)