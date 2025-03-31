import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model and vectorizer
model = joblib.load("logistic_regression_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")  # Load the saved vectorizer

# Streamlit UI
st.set_page_config(page_title="Phishing Email Detector", page_icon="🚨", layout="centered")
st.title("🔍 Phishing Email Detector")
st.markdown("## Detect Phishing Emails Instantly! 📨")
st.write("Paste an email body below and find out if it's **phishing** or **legitimate**.")

# Text input for email body
email_text = st.text_area("📩 Enter the email content:", height=200, placeholder="Paste the email text here...")

# Add a stylish button
if st.button("🚀 Check Now", use_container_width=True):
    if email_text.strip():
        # Convert input text to TF-IDF representation
        email_tfidf = vectorizer.transform([email_text])

        # Make prediction
        prediction = model.predict(email_tfidf)[0]
        
        # Display result with color emphasis
        if prediction == 1:
            st.error("🛑 **Phishing Email**! Be cautious.")
        else:
            st.success("✅ **Legitimate Email**. No threats detected.")
    else:
        st.warning("⚠️ Please enter an email body to analyze.")
