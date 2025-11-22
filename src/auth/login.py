import streamlit as st

def login_screen():
    password = st.text_input("Enter access password", type="password")
    if password == "TestAccess2025":
        return True
    elif password:
        st.error("Invalid password")
    return False
