
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊")

st.title("📊 Customer Churn Prediction")

if not Path("model.pkl").exists() or not Path("preprocessor.pkl").exists():
    st.warning(
        "model.pkl and/or preprocessor.pkl were not found. "
        "Train your model first and save them with joblib."
    )
    st.stop()

model = joblib.load("model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

st.write("Enter customer information:")

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure (months)", 0, 100, 12)
monthly = st.number_input("Monthly Charges", 0.0, 500.0, 70.0)
total = st.number_input("Total Charges", 0.0, 100000.0, 1000.0)

if st.button("Predict"):
    st.info(
        "Replace the DataFrame below with ALL features used during training. "
        "This template only demonstrates deployment."
    )
    data = pd.DataFrame({
        "Gender":[gender],
        "Senior Citizen":[senior],
        "Partner":[partner],
        "Dependents":[dependents],
        "Tenure Months":[tenure],
        "Monthly Charges":[monthly],
        "Total Charges":[total],
    })
    try:
        X = preprocessor.transform(data)
        pred = model.predict(X)[0]
        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(X)[0][1]
            st.metric("Churn Probability", f"{prob:.1%}")
        if pred == 1:
            st.error("Likely to churn")
        else:
            st.success("Not likely to churn")
    except Exception as e:
        st.exception(e)
