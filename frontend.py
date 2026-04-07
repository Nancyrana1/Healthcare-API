import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Insurance Predictor")

st.title("💰 Insurance Premium Predictor")

# Inputs
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Smoker?", [True, False])
city = st.text_input("City", "Mumbai")

occupation = st.selectbox(
    "Occupation",
    ['retired','freelancer','student','government_job','business_owner','unemployed','private_job']
)

# Button
if st.button("Predict"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        response = requests.post(API_URL, json=input_data)

        st.write("Status Code:", response.status_code)
        st.write("Raw Response:", response.text)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Category: {result['predicted_category']}")
        else:
            st.error("API error")

    except Exception as e:
        st.error(f"Error: {e}")