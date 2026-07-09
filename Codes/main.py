import streamlit as st
import pandas as pd
import requests
from io import BytesIO

# The URL where your Flask API is running
prediction_endpoint = "http://127.0.0.1:5000/predict"

# 1. Page Configuration (Makes it look wider and sets the browser tab title)
st.set_page_config(page_title="Sentiment Analyzer", page_icon="🧠", layout="centered")

# 2. Main Title and Subtitle
st.title("🧠 Customer Sentiment Analyzer")
st.markdown("Analyze customer feedback instantly using our NLP Machine Learning model.")
st.divider() # Adds a clean horizontal line

# 3. Create two tabs to separate the features cleanly
tab1, tab2 = st.tabs(["💬 Single Text Analysis", "📁 Bulk CSV Analysis"])

with tab1:
    st.subheader("Analyze a Single Review")
    user_input = st.text_area("Paste the customer review below:", placeholder="E.g., I absolutely loved this product, highly recommend!")
    
    if st.button("Predict Sentiment", type="primary"):
        if user_input.strip() == "":
            st.warning("Please enter some text before predicting.")
        else:
            with st.spinner('Analyzing sentiment...'):
                # BUG FIX: changed 'data' to 'json' to match the Flask backend
                response = requests.post(prediction_endpoint, json={"text": user_input})
                
                if response.status_code == 200:
                    result = response.json().get('prediction')
                    if result == "Positive":
                        st.success(f"**Result:** This is a {result} review! 🌟")
                    else:
                        st.error(f"**Result:** This is a {result} review. ⚠️")
                else:
                    st.error("Error connecting to the backend API.")

with tab2:
    st.subheader("Bulk Analysis")
    st.markdown("Upload a CSV file containing a column named **'Sentence'**.")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if st.button("Analyze CSV File", type="primary"):
        if uploaded_file is not None:
            with st.spinner('Processing bulk data...'):
                file = {"file": uploaded_file}
                response = requests.post(prediction_endpoint, files=file)
                
                if response.status_code == 200:
                    st.success("Analysis Complete!")
                    response_bytes = BytesIO(response.content)
                    
                    st.download_button(
                        label="📥 Download Annotated CSV",
                        data=response_bytes,
                        file_name="Sentiment_Predictions.csv",
                        mime="text/csv",
                    )
                else:
                    st.error("Error processing the file.")
        else:
            st.warning("Please upload a file first.")