import streamlit as st

st.title("Calculator App using Streamlit")

st.write("---")

num1 = st.number_input(lebal="Enter first number")
num2 = st.number_input(lebal="Enter second number")
st.write("Operation")

operation = st.radio("Select an operation to perform:")



