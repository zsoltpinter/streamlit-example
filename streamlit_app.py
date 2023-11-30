import streamlit as st
import setuptools
 
st.title("Szamologep a Streamliten")
 
# creates a horizontal line
st.write("---")
 
# input 1
num1 = st.number_input(label="Enter first number")
 
# input 2
num2 = st.number_input(label="Enter second number")
 
st.write("Operation")
 
operation = st.radio("Select an operation to perform:",
                    ("Add", "Subtract", "Multiply", "Divide"))
 
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
 
if st.button("Calculate result"):
    calculate()

ads = st.slider("ketto hatvanyai", 1, 10)
st.write(2**ads)

setuptools.setup(
    name="streamlit-awesome-table",
    version="0.1.0",
    author="Caio Fábio de Araujo",
    author_email="caiofaar@gmail.com",
    description="Awesome Table is a component to display a table in Streamlit with search and order.",
    long_description="Display a table with search and order components that will be display above the table or in sidebar.",
    long_description_content_type="text/plain",
    url="https://github.com/caiodearaujo/streamlit-awesome-table",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
        "pandas"
    ],
)
