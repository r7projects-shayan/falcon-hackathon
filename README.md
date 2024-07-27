# Healthcare AI System

A system leveraging AI for remote healthcare, including features for AI chatbot diagnosis, drug identification, doctors handwriting identification.

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
    git clone https://github.com/djpapzin/healthcare-ai-system.git
    cd healthcare-ai-system
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Backend

1. Navigate to the backend directory:
    ```bash
    cd backend
    ```

2. Run the Django server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

### Running the Frontend

1. Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2. Run the Streamlit app:
    ```bash
    streamlit run home.py
    ```

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
