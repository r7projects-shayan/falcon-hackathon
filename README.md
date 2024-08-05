# Healthcare AI System

A system leveraging AI for remote healthcare, including features for AI chatbot diagnosis, drug identification, doctors handwriting identification.

## Demo

A live demo of the application is available at: https://healthcare-ai-falcon-hackathon.streamlit.app/

## Project Structure

- `frontend`: Contains the Streamlit frontend code.
- `backend`: Contains the Django backend code.

## Getting Started

### Prerequisites

- Python 3.x
- Django
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

### Running the Backend

1. Navigate to the backend directory:
    ```bash
    cd backend
    ```

2. Run the Django migrations:
    ```bash
    python manage.py migrate
    ```

3. Run the Django server:
    ```bash
    python manage.py runserver
    ```

    Django server will start at: http://127.0.0.1:8000/

### Running the Frontend

1. Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
    Streamlit server will start at: http://localhost:8501

## AI71 Basic Chat Functionality

This project now includes basic chat functionality using the AI71 platform. This feature allows users to interact with an AI chatbot for various purposes, such as answering questions or providing assistance.

### How to Use

1. Start the application.
2. Access the chat interface.
3. Type your questions or messages.
4. Receive responses from the AI71-powered chatbot.

### Requirements

- [AI71 API Key](https://marketplace.ai71.ai/api-keys)
- [AI71 documntation](https://marketplace.ai71.ai/documentation)

## Doctor's Handwriting Identification and OCR

This project includes functionality to identify and process doctor's handwriting from prescription images. It uses an AI model to detect bounding boxes around handwritten text and classify each character. The classified characters are then combined to form the extracted text, which is further processed by an OCR model to convert it into digital text.

### How to Use

1. Start the application.
2. Navigate to the "Drug Identification" page.
3. Upload a prescription image.
4. Click the "Process Prescription" button.
5. The application will display the processed image with bounding boxes and labels, along with the extracted digital text.

### Requirements

- Inference API URL and Key (set in environment variables)

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
