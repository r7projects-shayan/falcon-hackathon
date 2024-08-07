# Healthcare System Dashboard - Streamlit Frontend

This is the frontend for our Healthcare System Dashboard, built using Streamlit.

## Demo

A live demo of the application is available at: https://healthcare-ai-falcon-hackathon.streamlit.app/


## Setup

1. Install required packages:
   ```
   pip install streamlit requests python-dotenv ai71
   ```

2. Set up your environment variables:
   Create a `.env` file in the same directory as your `app.py` with the following content:
   ```
   AI71_API_KEY=your_api_key_here
   ```

3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Features

- Home page with AI71-powered chat interface
- AI Chatbot Diagnosis page
- Drug Identification page
- Outbreak Alert page

## Usage

- Navigate to the Home tab to interact with the AI71 chatbot.
- Use the sidebar to switch between different features.

## Note

Ensure that your Django backend is running on `http://localhost:8000` for the API calls to work correctly.