import os
import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="AI Food Analyzer", layout="wide", page_icon="🍏")

# Use environment variable for backend URL (Best Practice for deployment)
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.title("🍏 AI-Based Food Nutrition Analyzer")
st.markdown("Analyze macros, get health scores, and ask custom nutrition questions.")

option = st.sidebar.radio("Choose a Feature", ("Analyze Food", "Ask a Question"))

if option == "Analyze Food":
    st.header("Detailed Food Analysis")
    food_item = st.text_input("Enter Food Item (e.g., Apple, Pizza, Paneer Tikka):")
    
    if st.button("Analyze", type="primary"):
        if food_item:
            with st.spinner("AI is analyzing the food..."):
                try:
                    response = requests.get(f"{BACKEND_URL}/analyze/{food_item}", timeout=15)
                    if response.status_code == 200:
                        data = response.json().get("data", {})
                        
                        st.subheader(f"Results for {food_item.capitalize()}")
                        st.write(data.get("explanation", ""))
                        
                        # Displaying Metrics efficiently
                        col1, col2, col3 = st.columns(3)
                        col1.metric("Health Score", f"{data.get('health_score', 0)} / 10")
                        col2.metric("Fiber", f"{data.get('fiber', 0)} g")
                        col3.metric("Pairing", data.get("suggested_pairing", "N/A"))
                        
                        st.divider()
                        
                        # Beautiful Macro Chart
                        st.subheader("Macro-Nutrients Breakdown")
                        df = pd.DataFrame({
                            'Nutrient': ['Protein', 'Fat', 'Carbs'], 
                            'Grams': [data.get('protein', 0), data.get('fat', 0), data.get('carbohydrates', 0)]
                        })
                        st.bar_chart(df.set_index('Nutrient'), color="#2E86C1")
                    else:
                        st.error("Could not fetch data. Please try again.")
                except requests.exceptions.RequestException:
                    st.error("Backend server is not running. Please start FastAPI.")

elif option == "Ask a Question":
    st.header("Ask from Knowledge Base (RAG)")
    question = st.text_input("Enter your question:")
    
    if st.button("Ask AI", type="primary"):
        if question:
            with st.spinner("Searching documents..."):
                try:
                    response = requests.get(f"{BACKEND_URL}/ask/{question}", timeout=30)
                    if response.status_code == 200:
                        st.success("Answer:")
                        st.info(response.json().get("answer", ""))
                    else:
                        st.error("Failed to get an answer.")
                except requests.exceptions.RequestException:
                    st.error("Backend server is not running.")

st.sidebar.markdown("---")
st.sidebar.caption("Developed with LlamaIndex & FastAPI | Engineering Project 2026")