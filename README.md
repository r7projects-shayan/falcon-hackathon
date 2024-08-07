# Healthcare AI System

A system leveraging AI for remote healthcare, including features for AI chatbot diagnosis, drug identification, doctors handwriting identification, and disease detection from chest X-ray images.

## Demo

A live demo of the application is available at: https://healthcare-ai-falcon-hackathon.streamlit.app/

## Project Structure

- `frontend`: Contains the Streamlit frontend code.
- `app_docr.py`: Contains code for doctor's handwriting detection and OCR.
- `app.py`: Contains code for disease detection and classification.
- `Symptoms Detection\app.py`: Contains code for symptom detection, precaution, and occurrence.
- `requirements.txt`: Lists the required Python packages.

## Getting Started

### Prerequisites

- Python 3.x
- Streamlit

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/r7projects-shayan/falcon-hackathon.git
    cd falcon-hackathon
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Setup environment variables:
    ```bash
    cp .env.example .env
    ```
    - Update the `.env` file with your AI71 API key and Roboflow API key.

### Running the Applications

1. **Frontend (Main Dashboard):**
    ```bash
    cd frontend
    streamlit run app.py
    ```
    Streamlit server will start at: http://localhost:8501

2. **Doctor's Handwriting Detection and OCR:**
    ```bash
    streamlit run app_docr.py
    ```

3. **Disease Detection and Classification:**
    ```bash
    streamlit run app.py
    ```

4. **Symptom Detection:**
    ```bash
    cd Symptoms Detection
    streamlit run app.py
    ```

## AI71 Basic Chat Functionality

This project includes basic chat functionality using the AI71 platform. This feature allows users to interact with an AI chatbot for various purposes, such as answering questions or providing assistance.

### How to Use

1. Start the application (`frontend\app.py`).
2. Navigate to the "AI Chatbot Diagnosis" page.
3. Type your questions or messages.
4. Receive responses from the AI71-powered chatbot.

### Requirements

- [AI71 API Key](https://marketplace.ai71.ai/api-keys)
- [AI71 documntation](https://marketplace.ai71.ai/documentation)

## Doctor's Handwriting Identification and OCR

This project includes functionality to identify and process doctor's handwriting from prescription images. It uses an AI model to detect bounding boxes around handwritten text and classify each character. The classified characters are then combined to form the extracted text, which is further processed by an OCR model to convert it into digital text.

### How to Use

1. Start the application (`app_docr.py`).
2. Upload a prescription image.
3. The application will display the processed image with bounding boxes and labels, along with the extracted digital text.

### Requirements

- Roboflow API Key (set in environment variables)

## Disease Detection and Classification

This project includes functionality to detect diseases from chest X-ray images using a pre-trained deep learning model.

### How to Use

1. Start the application (`app.py`).
2. Upload a chest X-ray image.
3. The application will display the image and the predicted disease class.

### Requirements

- `FINAL_MODEL.keras` (ensure it's in the same directory as `app.py`)

## Symptom Detection, Precaution, and Occurrence

This project includes functionality to detect diseases based on user-entered symptoms. It also provides precautions and occurrence information for the detected disease.

### How to Use

1. Start the application (`Symptoms Detection\app.py`).
2. Enter your symptoms, separated by commas.
3. The application will display the predicted disease, precautions, and occurrence information.

### Requirements

- `training_data.csv`, `Symptom2Disease.csv`, `disease_precaution.csv`, `disease_riskFactors.csv` (ensure these files are in the `Symptoms Detection` directory)

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
