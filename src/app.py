import streamlit as st
from auth.login import login
from ui.layout import render_main_ui

if login():
    render_main_ui()