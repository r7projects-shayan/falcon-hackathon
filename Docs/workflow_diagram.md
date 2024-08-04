```mermaid
graph TD
  A[User Uploads Prescription Image] --> B[Backend Receives Image]
  B --> C[Call Doctor's Handwriting Detection API]
  C --> D[API Detects Bounding Boxes & Classes]
  D --> E[Extract Bounding Boxes & Classes]
  E --> F[Call OCR Model]
  F --> G[OCR Model Returns Detected Text]
  G --> H[Send Text to Falcon LLM Model via AI71 API]
  H --> I[Falcon LLM Model Processes Text]
  I --> J[Return Processed Text to Backend]
  J --> K[Send Final Results to Frontend]
  K --> L[Display Results in Streamlit App]