import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import requests
from utils.ai71_utils import get_ai71_response
from datetime import datetime
import cv2
import numpy as np
from PIL import Image
from inference_sdk import InferenceHTTPClient
import supervision as sv
import matplotlib.pyplot as plt
import io

st.title("Healthcare System Dashboard")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "AI Chatbot Diagnosis", "Drug Identification", "Outbreak Alert"])

# Initialize the Inference Client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="LSbJ0tl3WTLn4Aqar0Sp"
)

def preprocess_image(image):
    # Convert PIL Image to OpenCV format
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Preprocessing steps (simplified for brevity)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    edges = cv2.Canny(binary, 100, 200)
    
    return edges

def get_x1(detection):
    return detection.xyxy[0][0]

if page == "Home":
    st.write("Welcome to the Healthcare System Dashboard!")
    
    # AI71 Chat Interface
    st.subheader("AI Assistant")
    user_input = st.text_input("You:", key="user_input")
    if st.button("Send"):
        if user_input:
            response = get_ai71_response(user_input)
            st.text_area("AI:", value=response, height=200, max_chars=None, key="ai_response")
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
    st.write("Upload a prescription image for drug identification.")
    uploaded_file = st.file_uploader("Upload prescription", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Prescription", use_column_width=True)

        if st.button("Process Prescription"):
            # Preprocess the image
            preprocessed_image = preprocess_image(image)
            
            # Perform inference
            result_doch1 = CLIENT.infer(preprocessed_image, model_id="doctor-s-handwriting/1")
            
            # Extract labels and detections
            labels = [item["class"] for item in result_doch1["predictions"]]
            detections = sv.Detections.from_inference(result_doch1)
            
            # Sort detections and labels
            sorted_indices = sorted(range(len(detections)), key=lambda i: get_x1(detections[i]))
            sorted_labels = [labels[i] for i in sorted_indices]
            
            # Convert list to string
            resulting_string = ''.join(sorted_labels)
            
            st.write("Extracted Text from Prescription:", resulting_string)
            
            # Prepare prompt for LLM
            prompt = f"""Analyze the following prescription text:
            {resulting_string}

            Please provide:
            1. Identified drug name(s)
            2. Full name of each identified drug
            3. Primary uses of each drug
            4. Common side effects
            5. Recommended dosage (if identifiable from the text)
            6. Any warnings or precautions
            7. Potential interactions with other medications (if multiple drugs are identified)
            8. Any additional relevant information for the patient

            If any part of the prescription is unclear or seems incomplete, please mention that and provide information about possible interpretations or matches. Always emphasize the importance of consulting a healthcare professional for accurate interpretation and advice."""
            
            # Get LLM response
            llm_response = get_ai71_response(prompt)
            
            st.subheader("AI Analysis of the Prescription")
            st.write(llm_response)

    else:
        st.info("Please upload a prescription image to proceed.")

elif page == "Outbreak Alert":
    st.write("This is the Outbreak Alert page.")
    # Add content for Outbreak Alert page