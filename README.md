# Phishing-Email-Detection

This is a Phishing Email Detection web app built with Streamlit. It allows users to enter an email subject and body to check if it is a phishing email or legitimate using a trained machine learning model.

🔥 Features

✅ Detect phishing emails based on subject and body content

✅ User-friendly web UI with Streamlit

✅ Generates word clouds and email pattern analysis

✅ Sharable link via Streamlit Community Cloud

🛠 Installation

1️⃣ Clone the repository:
git clone https://github.com/your-username/phishing-email-detector.git
cd phishing-email-detector

2️⃣ Install dependencies:
pip install -r requirements.txt

3️⃣ Run the Streamlit app:
streamlit run app.py
This will open the app in your browser at http://localhost:8501/.



🚀 Deployment on Streamlit Community Cloud

Steps to Deploy:

Push your project to GitHub
Go to Streamlit Cloud
Click "New App" → Select your GitHub repository
Set the main file as app.py
Click "Deploy" → Get a public link 🎉


📊 Dataset

The model is trained using real & synthetic phishing emails, including:

CEAS_08.csv (Real-world phishing emails)

Synthetic dataset (AI-generated phishing templates)

Each email contains:

Sender, Receiver, Date, Subject, Body, URL Count, Label (Phishing/Legit)

