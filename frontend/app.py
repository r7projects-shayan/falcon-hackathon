import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import requests
from utils.ai71_utils import get_ai71_response
from datetime import datetime

st.title("Healthcare System Dashboard")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "AI Chatbot Diagnosis", "Drug Identification", "Outbreak Alert"])

if page == "Home":
    st.write("Welcome to the Healthcare System Dashboard!")
    
    # AI71 Chat Interface
    st.subheader("AI Assistant")
    user_input = st.text_input("You:", key="user_input")
    if st.button("Send"):
        if user_input:
            response = get_ai71_response(user_input)
            st.text_area("AI:", value=response, height=100, max_chars=None, key="ai_response")
        else:
            st.warning("Please enter a message.")

elif page == "AI Chatbot Diagnosis":
    st.write("This is the AI Chatbot Diagnosis page.")
    if st.button("Get Diagnosis"):
        response = requests.get("http://localhost:8000/api/diagnosis/")
        if response.status_code == 200:
            st.write(response.json())
        else:
            st.write("Failed to fetch diagnosis.")

elif page == "Drug Identification":
    uploaded_file = st.file_uploader("Upload prescription", type=["png","jpeg"])


    if uploaded_file is None:
        st.info(f"""
                👆 Upload your prescription image first.
                """)



    if st.button("Send Prescription"):

        url = 'http://localhost:8000/api/upload_drug_prescription/'

        response = requests.post(url,data={'created':datetime.now(), 'name':'myfile'}, files={'file': uploaded_file})

        if response.status_code == 201:
            st.write("Image uploaded!")
            # switch_page("app")
            

        else:
            st.write(response.status_code)

elif page == "Outbreak Alert":
    st.write("This is the Outbreak Alert page.")
    # Add content for Outbreak Alert page
