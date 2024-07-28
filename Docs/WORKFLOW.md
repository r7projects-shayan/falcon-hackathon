## Updated Workflow Steps

1. **User Uploads Prescription Image**
   - **Frontend**: User uploads an image via the Streamlit app.
   - **Action**: Image is sent to the backend.

2. **Backend Receives Image**
   - **Backend**: Django server receives the image.
   - **Action**: Backend calls the Doctor's Handwriting Detection API.

3. **Doctor's Handwriting Detection API**
   - **API**: Image is processed to detect bounding boxes and classes.
   - **Action**: Bounding boxes and classes are returned to the backend.

4. **Backend Calls OCR Model**
   - **Backend**: Extract bounding boxes and classes from API response.
   - **Action**: Send bounding boxes to an OCR model to convert to text. DocTR (via Roboflow Hosted API)

5. **Backend Processes OCR Text**
   - **Backend**: OCR model returns detected text.
   - **Action**: Send text to Falcon LLM model via AI71 API.

6. **Falcon LLM Model via AI71 API**
   - **API**: Text is processed for context understanding.
   - **Action**: Processed text is returned to the backend.

7. **Backend Sends Final Results to Frontend**
   - **Backend**: Final processed text received from AI71 API.
   - **Action**: Send final results to the frontend