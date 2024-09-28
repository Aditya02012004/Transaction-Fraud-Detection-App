import joblib
import streamlit as st

model = joblib.load('Final Transactions.pkl')

# Title of the app
st.title("Transaction Fraud Detection App")

# Creating a text input for user input
# Input fields
Unamed_0 = st.number_input("Serial No")
transaction_id = st.number_input("Transaction ID")
customer_id = st.number_input("Customer ID")
terminal_id = st.number_input("Terminal ID")
tx_amount = st.number_input("Transaction Amount")
tx_time_seconds = st.number_input("Transaction Time (in seconds)")
tx_time_days = st.number_input("Transaction Time (in days)")
tx_fraud_scenario = st.number_input("Fraud Scenario")
tx_date = st.number_input("Transaction Date (YYYYMMDD)")
tx_time = st.number_input("Transaction Time (HHMMSS)")

# Make prediction
if st.button("Predict"):
    input_data = [[Unamed_0, transaction_id, customer_id, terminal_id, tx_amount,
                   tx_time_seconds, tx_time_days, tx_fraud_scenario,
                   tx_date, tx_time]]
    prediction = model.predict(input_data)

    if prediction[0] == 0:
        st.success("Normal Transaction")
    else:
        st.error("Fraud Transaction")
