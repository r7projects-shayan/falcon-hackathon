import streamlit as st
import requests
from utils.ai71_utils import get_ai71_response
from datetime import datetime
import cv2
import numpy as np
from PIL import Image
import supervision as sv
import matplotlib.pyplot as plt
import io
import os
from inference_sdk import InferenceHTTPClient

st.title("Healthcare System Dashboard")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "AI Chatbot Diagnosis", "Drug Identification", "Outbreak Alert"])

# Access secrets using st.secrets
if "INFERENCE_API_URL" not in st.secrets or "INFERENCE_API_KEY" not in st.secrets:
    st.error("Please make sure to set your secrets in the Streamlit secrets settings.")
else:
    # Initialize the Inference Client
    CLIENT = InferenceHTTPClient(
        api_url=st.secrets["INFERENCE_API_URL"],
        api_key=st.secrets["INFERENCE_API_KEY"]
    )

    # Function to preprocess the image
    def preprocess_image(image_path):
        # Load the image
        image = cv2.imread(image_path)
        
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Remove noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Thresholding/Binarization
        _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Dilation and Erosion
        kernel = np.ones((1, 1), np.uint8)
        dilated = cv2.dilate(binary, kernel, iterations=1)
        eroded = cv2.erode(dilated, kernel, iterations=1)
        
        # Edge detection
        edges = cv2.Canny(eroded, 100, 200)
        
        # Deskewing
        coords = np.column_stack(np.where(edges > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        
        (h, w) = edges.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        deskewed = cv2.warpAffine(edges, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        
        # Find contours
        contours, _ = cv2.findContours(deskewed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Draw contours on the original image
        contour_image = image.copy()
        cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
        
        return contour_image

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
                # Save the image to a temporary file
                temp_image_path = "temp_image.jpg"
                image.save(temp_image_path)
                
                # Preprocess the image
                preprocessed_image = preprocess_image(temp_image_path)

                # Perform inference
                result_doch1 = CLIENT.infer(preprocessed_image, model_id="doctor-s-handwriting/1")
                
                # Extract labels and detections
                labels = [item["class"] for item in result_doch1["predictions"]]
                detections = sv.Detections.from_inference(result_doch1)
                
                # Sort detections and labels
                sorted_indices = sorted(range(len(detections)), key=lambda i: get_x1(detections[i]))
                sorted_detections = [detections[i] for i in sorted_indices]
                sorted_labels = [labels[i] for i in sorted_indices]
                
                # Convert list to string
                resulting_string = ''.join(sorted_labels)
                
                # Display results
                st.subheader("Processed Prescription")
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
                
                # Plot bounding boxes
                image_with_boxes = preprocessed_image.copy()
                for detection in sorted_detections:
                    x1, y1, x2, y2 = detection.xyxy[0]
                    cv2.rectangle(image_with_boxes, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
                ax1.imshow(cv2.cvtColor(image_with_boxes, cv2.COLOR_BGR2RGB))
                ax1.set_title("Bounding Boxes")
                ax1.axis('off')
                
                # Plot labels
                image_with_labels = preprocessed_image.copy()
                for i, detection in enumerate(sorted_detections):
                    x1, y1, x2, y2 = detection.xyxy[0]
                    label = sorted_labels[i]
                    cv2.putText(image_with_labels, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                ax2.imshow(cv2.cvtColor(image_with_labels, cv2.COLOR_BGR2RGB))
                ax2.set_title("Labels")
                ax2.axis('off')
                
                st.pyplot(fig)
                
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

                # Remove the temporary image file
                os.remove(temp_image_path)

        else:
            st.info("Please upload a prescription image to proceed.")

    elif page == "Outbreak Alert":
        st.write("This is the Outbreak Alert page.")
        # Add content for Outbreak Alert page
