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
from bs4 import BeautifulSoup
import tensorflow as tf
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK data (only needs to be done once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# --- Preprocess text function (moved outside session state) ---
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    cleaned_text = re.sub(r'[^a-zA-Z0-9\s\,]', ' ', text)
    # Tokenize text
    tokens = word_tokenize(cleaned_text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Rejoin tokens into a single string
    cleaned_text = ' '.join(tokens)

    return cleaned_text

st.title("Medi Scape Dashboard")

# --- Session State Initialization ---
if 'disease_model' not in st.session_state:
    try:
        st.session_state.disease_model = tf.keras.models.load_model('FINAL_MODEL.keras')
    except FileNotFoundError:
        st.error("Disease classification model not found. Please ensure 'FINAL_MODEL.keras' is in the same directory as this app.")
        st.session_state.disease_model = None

# --- Load the vectorizer regardless of the model_llm's state ---
if 'vectorizer' not in st.session_state:
    st.session_state.vectorizer = CountVectorizer()
    vectorizer_path = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")  # Updated path
    st.session_state.vectorizer = pd.read_pickle(vectorizer_path)

if 'model_llm' not in st.session_state:
    # --- Code from LLMs/LLMs_chatbot.ipynb ---
    # Load pre-trained model and vectorizer (replace with your actual file paths)
    st.session_state.model_llm = LogisticRegression()
    st.session_state.model_llm = pd.read_pickle("LLMs/logistic_regression_model.pkl")  

    # Load datasets (only for reference, not used for training)
    dataset_1 = pd.read_csv("Symptoms_Detection/training_data.csv")
    dataset_2 = pd.read_csv("Symptoms_Detection/Symptom2Disease.csv")

    # Create symptoms_text column (only for reference, not used for training)
    dataset_1['symptoms_text'] = dataset_1.apply(lambda row: ','.join([col for col in dataset_1.columns if row[col] == 1]), axis=1)
    final_dataset = pd.DataFrame(dataset_1[["prognosis", "symptoms_text"]])
    final_dataset.columns = ['label', 'text']

    # Combine datasets (only for reference, not used for training)
    df_combined = pd.concat([final_dataset, dataset_2[['label', 'text']]], axis=0, ignore_index=True)

    # Store in session state (only for reference, not used for training)
    st.session_state.df_combined = df_combined
# --- End of Session State Initialization ---

# Load the disease classification model
try:
    disease_model = tf.keras.models.load_model('FINAL_MODEL.keras')
except FileNotFoundError:
    st.error("Disease classification model not found. Please ensure 'FINAL_MODEL.keras' is in the same directory as this app.")
    disease_model = None

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "AI Chatbot Diagnosis", "Drug Identification", "Disease Detection", "Outbreak Alert"])

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

    # --- Prediction function (using session state) ---
    def predict_disease(symptoms):
        preprocessed_symptoms = preprocess_text(symptoms)
        symptoms_vectorized = st.session_state.vectorizer.transform([preprocessed_symptoms])
        prediction = st.session_state.model_llm.predict(symptoms_vectorized)
        return prediction[0]

    # --- New function to analyze X-ray with LLM ---
    def analyze_xray_with_llm(predicted_class):
        prompt = f"""
        Based on a chest X-ray analysis, the predicted condition is {predicted_class}. 
        Please provide a concise summary of this condition, including:
        - A brief description of the condition.
        - Common symptoms associated with it.
        - Potential causes.
        - General treatment approaches.
        - Any other relevant information for a patient.
        """
        llm_response = get_ai71_response(prompt)
        st.write("## LLM Analysis of X-ray Results:")
        st.write(llm_response)

    if page == "Home":
        st.markdown("## Project Overview")
        st.write("This healthcare application allows users to upload prescription images, which are then processed to extract and analyze the text. The key components include image processing, text recognition, and context understanding using machine learning models.")

        st.markdown("## Features")
        st.write("This application provides various AI-powered tools for remote healthcare, including:")
        features = [
            "**AI Chatbot Diagnosis:** Interact with an AI chatbot for preliminary diagnosis and medical information.",
            "**Drug Identification:** Upload a prescription image to identify medications and access relevant details.",
            "**Doctor's Handwriting Identification:** Our system can accurately recognize and process doctor's handwriting.",
            "**Disease Detection:** Upload a chest X-ray image to detect potential diseases.",
            "**Outbreak Alert:** Stay informed about potential disease outbreaks in your area."
        ]
        for feature in features:
            st.markdown(f"- {feature}")

        st.markdown("## How it Works")
        steps = [
            "**Upload:** You can upload a prescription image for drug identification or a chest X-ray image for disease detection.",
            "**Process:** Our AI models will analyze the image and extract relevant information.",
            "**Results:** You will receive identified drug names, uses, side effects, and more, or a potential disease diagnosis."
        ]
        for i, step in enumerate(steps, 1):
            st.markdown(f"{i}. {step}")

        st.markdown("## Key Features")
        key_features = [
            "**AI-Powered:** Leverages advanced AI models for accurate analysis and diagnosis.",
            "**User-Friendly:** Simple and intuitive interface for easy navigation and interaction.",
            "**Secure:** Your data is protected and handled with confidentiality."
        ]
        for feature in key_features:
            st.markdown(f"- {feature}")

        st.markdown("Please use the sidebar to navigate to different features.")

    elif page == "AI Chatbot Diagnosis":
        st.write("Enter your symptoms separated by commas:")
        symptoms_input = st.text_area("Symptoms:")
        if st.button("Diagnose"):
            if symptoms_input:
                # --- Pipeline 1 Implementation ---
                # 1. Symptom Input (already done with st.text_area)
                # 2. Regression Prediction
                regression_prediction = predict_disease(symptoms_input)

                # 3. LLM Prompt Enhancement
                prompt = f"""The predicted condition based on a symptom analysis is {regression_prediction}. 
                Provide a detailed explanation of this condition, including possible causes, common symptoms, 
                and general treatment approaches. Also, suggest when a patient should consult a doctor."""

                # 4. LLM Output
                llm_response = get_ai71_response(prompt)

                # 5. Combined Output
                st.write("## Logistic Regression Prediction:")
                st.write(regression_prediction)

                st.write("## LLM Explanation:")
                st.write(llm_response)
                # --- End of Pipeline 1 Implementation ---

            else:
                st.write("Please enter your symptoms.")

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

    elif page == "Disease Detection":
        st.write("Upload a chest X-ray image for disease detection.")
        uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_image is not None and st.session_state.disease_model is not None:
            # Display the image
            img_opened = Image.open(uploaded_image).convert('RGB')
            image_pred = np.array(img_opened)
            image_pred = cv2.resize(image_pred, (150, 150))

            # Convert the image to a numpy array
            image_pred = np.array(image_pred)

            # Rescale the image (if the model was trained with rescaling)
            image_pred = image_pred / 255.0

            # Add an extra dimension to match the input shape (1, 150, 150, 3)
            image_pred = np.expand_dims(image_pred, axis=0)

            # Predict using the model
            prediction = st.session_state.disease_model.predict(image_pred)

            # Get the predicted class
            predicted_ = np.argmax(prediction)

            # Decode the prediction
            if predicted_ == 0:
                predicted_class = "Covid"
            elif predicted_ == 1:
                predicted_class = "Normal Chest X-ray"
            else:
                predicted_class = "Pneumonia"

            st.image(image_pred, caption='Input image by user', use_column_width=True)
            st.write("Prediction Classes for different types:")
            st.write("COVID: 0")
            st.write("Normal Chest X-ray: 1")
            st.write("Pneumonia: 2")
            st.write("\n")
            st.write("DETECTED DISEASE DISPLAY")
            st.write(f"Predicted Class : {predicted_}")
            st.write(predicted_class)

            # Analyze X-ray results with LLM
            analyze_xray_with_llm(predicted_class)
        else:
            st.write("Please upload an image file or ensure the disease model is loaded.")

    elif page == "Outbreak Alert":
        st.markdown("## **Disease Outbreak News (from WHO)**")

        # Fetch WHO news page
        url = "https://www.who.int/news-room/events"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find news articles (adjust selectors if WHO website changes)
        articles = soup.find_all('div', class_='list-view--item')

        for article in articles[:5]:  # Display the top 5 news articles
            title_element = article.find('a', class_='link-container')
            if title_element:
                title = title_element.text.strip()
                link = title_element['href']
                date_element = article.find('span', class_='date')
                date = date_element.text.strip() if date_element else "Date not found"
                
                # Format date
                date_parts = date.split()
                if len(date_parts) >= 3:
                    try:
                        formatted_date = datetime.strptime(date, "%d %B %Y").strftime("%Y-%m-%d")
                    except ValueError:
                        formatted_date = date  # Keep the original date if formatting fails
                else:
                    formatted_date = date
                
                # Display news item in a card-like container
                with st.container():
                    st.markdown(f"**{formatted_date}**")
                    st.markdown(f"[{title}]({link})")
                    st.markdown("---")
            else:
                st.write("Could not find article details.")

# Auto-scroll to the bottom of the chat container
st.markdown(
    """
    <script>
    const chatContainer = document.querySelector('.st-chat-container');
    if (chatContainer) {
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
    </script>
    """,
    unsafe_allow_html=True,
)
