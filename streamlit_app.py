import streamlit as st

st.title("Calculator App using Streamlit")

st.write("---")

num1 = st.number_input(label="Enter first number")
num2 = st.number_input(label="Enter second number")
st.write("Operation")

operation = st.radio("Select an operation to perform:",("Összeadás", "Kivonás", "Szorzás", "Osztás"))

ans = 0

def calculate():
    if operation == "Add":
        ans = num1 + num2
    elif operation == "Subtract":
        ans = num1 - num2
    elif operation == "Multiply":
        ans = num1 * num2
    elif operation=="Divide" and num2!=0:
        ans = num1 / num2
    else:
        st.warning("Division by 0 error. Please enter a non-zero number.")
        ans = "Not defined"

    st.success(f"Answer = {ans}")
    



