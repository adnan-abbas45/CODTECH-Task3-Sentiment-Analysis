# CODTECH IT Solutions - Task 3: Customer Sentiment Analysis

**Name:** Adnan Abbas  
**Intern ID:** [Insert Your ID Here]  
**Domain:** Data Analytics  

## Project Overview
This project is an end-to-end Machine Learning pipeline that analyzes customer reviews and predicts sentiment (Positive or Negative). It features a custom-trained XGBoost NLP model deployed via a Flask backend API, connected to an interactive, user-friendly Streamlit web interface. 

## Key Features & Techniques
- **Natural Language Processing (NLP):** Utilized `nltk` (PorterStemmer, Stopwords) and `CountVectorizer` to clean and tokenize raw text data.
- **Machine Learning:** Trained and tuned an XGBoost classifier to categorize sentiment, utilizing custom probability thresholds to handle real-world dataset imbalances.
- **Full-Stack Deployment:** Built a two-part architecture with a REST API (`Flask`) serving predictions to a dynamic frontend web application (`Streamlit`).
- **Bulk Processing:** Engineered a feature allowing users to upload CSV files of unlabelled reviews and download a fully annotated dataset with sentiment predictions.

## Technologies Used
- **Python:** Primary programming language.
- **Scikit-Learn & XGBoost:** Model training, scaling, and prediction.
- **Flask:** Backend API server.
- **Streamlit:** Interactive frontend UI.

## Repository Contents
- `api.py`: The Flask server and text-preprocessing engine.
- `main.py`: The Streamlit web application.
- `Models/`: Serialized `.pkl` files of the trained model, vectorizer, and scaler.
- `Screenshots`: Visual proof of the working web interface.
