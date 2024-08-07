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
import re  # Import the 're' module for regular expressions
from nltk.tokenize import word_tokenize  # Import word_tokenize
from nltk.corpus import stopwords  # Import stopwords

# Download NLTK data (only needs to be done once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

st.title("Healthcare System Dashboard")

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

    # --- Code from LLMs/LLMs_chatbot.ipynb ---
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

    # Load datasets
    dataset_1 = pd.read_csv("Symptoms_Detection/training_data.csv")
    dataset_2 = pd.read_csv("Symptoms_Detection/Symptom2Disease.csv")

    # Create symptoms_text column
    dataset_1['symptoms_text'] = dataset_1.apply(lambda row: ','.join([col for col in dataset_1.columns if row[col] == 1]), axis=1)
    final_dataset = pd.DataFrame(dataset_1[["prognosis", "symptoms_text"]])
    final_dataset.columns = ['label', 'text']

    # Combine datasets
    df_combined = pd.concat([final_dataset, dataset_2[['label', 'text']]], axis=0, ignore_index=True)

    # Preprocess text data
    df_combined["cleaned_text"] = df_combined["text"].apply(preprocess_text)

    # Split data and train model
    X = df_combined['cleaned_text']
    y = df_combined['label']
    vectorizer = CountVectorizer()
    X_vectorized = vectorizer.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)
    model_llm = LogisticRegression()
    model_llm.fit(X_train, y_train)

    # Prediction function
    def predict_disease(symptoms):
        preprocessed_symptoms = preprocess_text(symptoms)
        symptoms_vectorized = vectorizer.transform([preprocessed_symptoms])
        prediction = model_llm.predict(symptoms_vectorized)
        return prediction[0]
    # --- End of code from LLMs/LLMs_chatbot.ipynb ---

    if page == "Home":
        st.write("Welcome to the Healthcare System Dashboard!")
        st.write("This application provides various AI-powered tools for remote healthcare, including:")
        st.write("- **AI Chatbot Diagnosis:** Interact with an AI chatbot for preliminary diagnosis and medical information.")
        st.write("- **Drug Identification:** Upload a prescription image to identify medications and access relevant details.")
        st.write("- **Doctor's Handwriting Identification:** Our system can accurately recognize and process doctor's handwriting.")
        st.write("- **Disease Detection:** Upload a chest X-ray image to detect potential diseases.")
        st.write("- **Outbreak Alert:** (Coming Soon) Stay informed about potential disease outbreaks in your area.")

        st.write("**How it Works:**")
        st.write("1. **Upload:** You can upload a prescription image for drug identification or a chest X-ray image for disease detection.")
        st.write("2. **Process:** Our AI models will analyze the image and extract relevant information.")
        st.write("3. **Results:** You will receive identified drug names, uses, side effects, and more, or a potential disease diagnosis.")

        st.write("**Key Features:**")
        st.write("- **AI-Powered:** Leverages advanced AI models for accurate analysis and diagnosis.")
        st.write("- **User-Friendly:** Simple and intuitive interface for easy navigation and interaction.")
        st.write("- **Secure:** Your data is protected and handled with confidentiality.")

        st.write("**Please use the sidebar to navigate to different features.**")

    elif page == "AI Chatbot Diagnosis":
        st.write("Enter your symptoms separated by commas:")
        symptoms_input = st.text_area("Symptoms:")
        if st.button("Predict"):
            if symptoms_input:
                prediction = predict_disease(symptoms_input)
                st.write(f"Predicted Disease: {prediction}")
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

        if uploaded_image is not None and disease_model is not None:
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
            prediction = disease_model.predict(image_pred)

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
        else:
            st.write("Please upload an image file or ensure the disease model is loaded.")

    elif page == "Outbreak Alert":
        st.write("## Disease Outbreak News (from WHO)")

        # Fetch WHO news page
        url = "https://www.who.int/news-room/events"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find news articles (adjust selectors if WHO website changes)
        articles = soup.find_all('div', class_='list-view--item')

        for article in articles[:5]: # Display the top 5 news articles
            title_element = article.find('a', class_='link-container')
            if title_element:
                title = title_element.text.strip()
                link = title_element['href']

                date_element = article.find('span', class_='date')
                date = date_element.text.strip() if date_element else "Date not found"

                # Extract date information and format it
                date_parts = date.split()
                if len(date_parts) >= 3:
                    try:
                        formatted_date = datetime.strptime(date, "%d %B %Y").strftime("%Y-%m-%d")
                    except ValueError:
                        formatted_date = date  # Keep the original date if formatting fails
                else:
                    formatted_date = date

                st.write(f"**[{formatted_date}]({link})**")
                st.write(f"{title}")
                st.write("---")
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
