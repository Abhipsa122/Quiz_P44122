# prompt: generate code for streamlit app 

import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = 'linear_regression_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Create a Streamlit app
st.title("Monthly Revenue Prediction")

# Input fields for user to enter data
st.header("Enter Store Details:")

website_traffic = st.number_input("Website Traffic:", min_value=0)
average_order_value = st.number_input("Average Order Value:", min_value=0.0)
customer_acquisition_cost = st.number_input("Customer Acquisition Cost:", min_value=0.0)
marketing_spend = st.number_input("Marketing Spend:", min_value=0.0)
customer_lifetime_value = st.number_input("Customer Lifetime Value:", min_value=0.0)


# Create a button to trigger prediction
if st.button("Predict Monthly Revenue"):
  # Prepare the input data as a DataFrame
  input_data = pd.DataFrame({
      'website_traffic': [website_traffic],
      'average_order_value': [average_order_value],
      'customer_acquisition_cost': [customer_acquisition_cost],
      'marketing_spend': [marketing_spend],
      'customer_lifetime_value': [customer_lifetime_value],
  })

  # Make the prediction using the loaded model
  predicted_revenue = loaded_model.predict(input_data)[0]

  # Display the predicted revenue
  st.header("Predicted Monthly Revenue:")
  st.write(f"{predicted_revenue:.2f}")
