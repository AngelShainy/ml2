import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("linear_regression_model.pkl")

st.title("Product Demand Prediction App")

st.write("Enter product and market details to predict")

# Inputs
Category = st.number_input("Category", value=1)
Region = st.number_input("Region", value=1)
Inventory = st.number_input("Inventory", value=200)
Sales = st.number_input("Sales", value=100)
Orders = st.number_input("Orders", value=50)
Price = st.number_input("Price", value=30.0)
Discount = st.number_input("Discount", value=10)
Weather = st.number_input("Weather", value=1)
Promotion = st.number_input("Promotion", value=0)
Competitor_Price = st.number_input("Competitor Price", value=30.0)
Seasonality = st.number_input("Seasonality", value=0)

# Prediction button
if st.button("Predict Demand"):

    input_data = np.array([[Category, Region, Inventory, Sales, Orders,
                            Price, Discount, Weather, Promotion,
                            Competitor_Price, Seasonality]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Demand: {prediction[0]}")