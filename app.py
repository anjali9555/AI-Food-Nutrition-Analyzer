import streamlit as st
import requests
import re
import pandas as pd

st.set_page_config(page_title="AI Food Analyzer", layout="wide")
BACKEND_URL = "http://localhost:8000"

st.title("AI-Based Food Nutrition Analyzer")

option = st.sidebar.selectbox("Choose a Feature", ("Analyze Food", "Ask a Question"))

# --- Robust Extraction Functions ---
def extract_macro(pattern, text):
    match = re.search(pattern, text, re.IGNORECASE)
    return float(match.group(1)) if match else 0

def extract_pairing(text):
    # 'Suggested Pairing:' ke baad ka text dhoondo
    match = re.search(r"Suggested Pairing:\s*(.*)", text, re.IGNORECASE)
    if match:
        # 1. Sirf pehli line lo
        line = match.group(1).split('\n')[0].strip()
        # 2. Agar AI ne lambi kahani shuru kar di hai, toh split kar do
        # Hum '.', 'Detailed', '---', ya extra spaces par cut lagayenge
        clean = re.split(r'\.|Detailed|---|provides|is an|A serving', line, flags=re.IGNORECASE)[0]
        return clean.strip().rstrip(':')
    return None

# --- Feature: Analyze Food ---
if option == "Analyze Food":
    st.header("Detailed Food Analysis")
    food_item = st.text_input("Enter Food Item:")
    
    if st.button("Analyze"):
        if food_item:
            with st.spinner("Analyzing..."):
                response = requests.get(f"{BACKEND_URL}/analyze/{food_item}")
                if response.status_code == 200:
                    nutrition_text = response.json().get("nutrition_info", "")
                    st.subheader(f"Results for {food_item.capitalize()}")
                    st.write(nutrition_text)

                    # Data Extraction
                    p = extract_macro(r"Protein:\s*(\d+\.?\d*)\s*g", nutrition_text)
                    f = extract_macro(r"Fat:\s*(\d+\.?\d*)\s*g", nutrition_text)
                    c = extract_macro(r"Carbohydrates:\s*(\d+\.?\d*)\s*g", nutrition_text)
                    fib = extract_macro(r"Fiber:\s*(\d+\.?\d*)\s*g", nutrition_text)
                    score = extract_macro(r"Health Score:\s*(\d+\.?\d*)", nutrition_text)
                    pairing = extract_pairing(nutrition_text)

                    # Charts
                    if any([p, f, c, fib]):
                        st.divider()
                        st.subheader("Macro-Nutrients Chart")
                        df = pd.DataFrame({'Nutrient': ['Protein', 'Fat', 'Carbs', 'Fiber'], 'Grams': [p, f, c, fib]})
                        st.bar_chart(df.set_index('Nutrient'))

                    # Score
                    if score > 0:
                        st.divider()
                        st.subheader("Health Rating")
                        st.metric(label="Overall Score", value=f"{score} / 10")

                    # Pairing (The Fix)
                    if pairing:
                        st.divider()
                        st.subheader("Suggested Pairing")
                        st.info(pairing)
                else:
                    st.error("Backend Error.")

elif option == "Ask a Question":
    st.header("Ask from Knowledge Base")
    question = st.text_input("Enter your question:")
    if st.button("Ask AI"):
        if question:
            response = requests.get(f"{BACKEND_URL}/ask/{question}")
            if response.status_code == 200:
                st.success("Answer:")
                st.write(response.json().get("answer", ""))

st.sidebar.markdown("---")
st.sidebar.write("Developed for Engineering Project 2026")