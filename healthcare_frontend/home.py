import streamlit as st
import requests

st.title("Healthcare System Dashboard")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "AI Chatbot Diagnosis", "Drug Identification", "Outbreak Alert"])

if page == "Home":
    st.write("Welcome to the Healthcare System Dashboard!")
elif page == "AI Chatbot Diagnosis":
    st.write("This is the AI Chatbot Diagnosis page.")
    if st.button("Get Diagnosis"):
        response = requests.get("http://localhost:8000/api/diagnosis/")
        if response.status_code == 200:
            st.write(response.json())
        else:
            st.write("Failed to fetch diagnosis.")
elif page == "Drug Identification":
    st.write("This is the Drug Identification page.")
    if st.button("Identify Drug"):
        response = requests.get("http://localhost:8000/api/drug/")
        if response.status_code == 200:
            st.write(response.json())
        else:
            st.write("Failed to fetch drug information.")
elif page == "Outbreak Alert":
    st.write("This is the Outbreak Alert page.")
    # Add content for Outbreak Alert page
