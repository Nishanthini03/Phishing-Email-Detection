import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model and vectorizer
model = joblib.load("logistic_regression_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")  # Load the saved vectorizer

# Streamlit UI
st.title("Phishing Email Detector")
st.write("Enter an email body to check if it's phishing or legitimate.")

# Text input for email body
email_text = st.text_area("Paste the email body here:")

if st.button("Check Email"):
    if email_text:
        # Convert input text to TF-IDF representation
        email_tfidf = vectorizer.transform([email_text])

        # Make prediction
        prediction = model.predict(email_tfidf)[0]
        result = "Phishing Email 🛑" if prediction == 1 else "Legitimate Email ✅"

        # Display result
        st.markdown(f"### Prediction: {result}")
    else:
        st.warning("Please enter an email body.")
