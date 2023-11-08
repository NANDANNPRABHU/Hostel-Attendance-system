import streamlit as st
from pages import notification, warden , student_details

st.set_page_config(page_title="Hostel Management", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Notification", "warden","Student details"])

if page == "Notification":
    notification.app()
elif page == "warden":
    warden.app()
elif page=="Student details":
    student_details.app()
