# prompt: generate code for streamlit app  for lasso model

import streamlit as st
import pandas as pd
import pickle

# Load the saved Lasso model
filename = 'lasso_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

# Create a Streamlit app
st.title("Monthly Revenue Prediction App")

# Input fields for user data
st.header("Enter Customer Data:")
customer_lifetime_value = st.number_input("Customer Lifetime Value")
average_order_value = st.number_input("Average Order Value")
number_of_orders = st.number_input("Number of Orders")
customer_acquisition_cost = st.number_input("Customer Acquisition Cost")
customer_retention_rate = st.number_input("Customer Retention Rate")
average_customer_lifespan = st.number_input("Average Customer Lifespan")
unique_product_purchased = st.number_input("Unique Products Purchased")
average_order_items = st.number_input("Average Order Items")
average_discount_applied = st.number_input("Average Discount Applied")


# Create a button to predict monthly revenue
if st.button("Predict Monthly Revenue"):
  # Create a DataFrame with the user input
  input_data = pd.DataFrame({
      'customer_lifetime_value': [customer_lifetime_value],
      'average_order_value': [average_order_value],
      'number_of_orders': [number_of_orders],
      'customer_acquisition_cost': [customer_acquisition_cost],
      'customer_retention_rate': [customer_retention_rate],
      'average_customer_lifespan': [average_customer_lifespan],
      'unique_product_purchased': [unique_product_purchased],
      'average_order_items': [average_order_items],
      'average_discount_applied': [average_discount_applied]
  })

  # Make the prediction using the loaded model
  predicted_revenue = loaded_model.predict(input_data)[0]

  # Display the predicted monthly revenue
  st.write(f"Predicted Monthly Revenue: ${predicted_revenue:.2f}")
