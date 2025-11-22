import streamlit as st

def login():
    st.sidebar.title("Login")
    password = st.sidebar.text_input("Password", type="password")
    return password == "TestAccess2025"