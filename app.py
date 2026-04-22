import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="House Price Prediction", layout="centered")

st.title("🏡 House Price Prediction App")
st.write("Enter house details to predict the price")

# Input fields
crim = st.number_input("CRIM")
zn = st.number_input("ZN")
indus = st.number_input("INDUS")
chas = st.number_input("CHAS")
nox = st.number_input("NOX")
rm = st.number_input("RM")
age = st.number_input("AGE")
dis = st.number_input("DIS")
rad = st.number_input("RAD")
tax = st.number_input("TAX")
ptratio = st.number_input("PTRATIO")
b = st.number_input("B")
lstat = st.number_input("LSTAT")

input_data = [[
    crim, zn, indus, chas, nox,
    rm, age, dis, rad, tax,
    ptratio, b, lstat
]]

prediction = model.predict(input_data)

# Prediction button
if st.button("Predict Price"):
    input_data = [[crim, zn, indus, chas, nox,rm, age, dis, rad, tax,ptratio, b, lstat]]
    prediction = model.predict(input_data)
    
    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")