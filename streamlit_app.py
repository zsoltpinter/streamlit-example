import streamlit as st

st.title("Calculator App using Streamlit")

st.write("---")

num1 = st.number_input(label="Enter first number")
num2 = st.number_input(label="Enter second number")
st.write("Operation")

operation = st.radio("Select an operation to perform:",("Összeadás", "Kivonás", "Szorzás", "Osztás"))

ans = 0

def calculate():
  if operation == "Összeadás":
    ans = num1 + num2
  elif operation == "Kivonás":
    ans = num1 - num2
  elif operation == "Szorzás":
    ans = num1 * num2
  elif operation == "Osztás" and num2!=0:
    ans = num1 / num2
  else:
    st.warning("Nem jó, szép volt majd legközelebb.")
    ans = "XDDD"

st.succes(f"Answer = {ans}")
    



