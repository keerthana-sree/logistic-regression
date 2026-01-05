import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("heart_disease_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("❤️ Heart Disease Prediction App")
st.write("Logistic Regression Model (Framingham Dataset)")

st.sidebar.header("Enter Patient Details")

# Inputs (same order as training data)
male = st.sidebar.selectbox("Gender", ("Female", "Male"))
age = st.sidebar.number_input("Age", min_value=1, max_value=120, value=45)
currentSmoker = st.sidebar.selectbox("Current Smoker", (0, 1))
cigsPerDay = st.sidebar.number_input("Cigarettes Per Day", min_value=0, max_value=100, value=0)
BPMeds = st.sidebar.selectbox("BP Medicines", (0, 1))
prevalentStroke = st.sidebar.selectbox("Stroke History", (0, 1))
prevalentHyp = st.sidebar.selectbox("Hypertension", (0, 1))
diabetes = st.sidebar.selectbox("Diabetes", (0, 1))
totChol = st.sidebar.number_input("Total Cholesterol", value=200)
sysBP = st.sidebar.number_input("Systolic BP", value=120)
diaBP = st.sidebar.number_input("Diastolic BP", value=80)
BMI = st.sidebar.number_input("BMI", value=25)
heartRate = st.sidebar.number_input("Heart Rate", value=75)
glucose = st.sidebar.number_input("Glucose", value=80)

# Convert gender
male = 1 if male == "Male" else 0

if st.button("Predict"):
    input_data = np.array([[male, age, currentSmoker, cigsPerDay, BPMeds,
                            prevalentStroke, prevalentHyp, diabetes,
                            totChol, sysBP, diaBP, BMI, heartRate, glucose]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Disease (Next 10 Years)")
    else:
        st.success("✅ Low Risk of Heart Disease")
