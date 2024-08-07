import os

# ... rest of the code ...

if 'vectorizer' not in st.session_state:
    st.session_state.vectorizer = CountVectorizer()
    vectorizer_path = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")
    st.session_state.vectorizer = pd.read_pickle(vectorizer_path)

# ... rest of the code ...
