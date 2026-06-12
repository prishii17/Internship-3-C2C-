import streamlit as st

st.title("CALCULATOR")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Addition"):
        st.success(f"Result = {num1 + num2}")
        st.balloons()

with col2:
    if st.button("Subtraction"):
        st.success(f"Result = {num1 - num2}")
        st.balloons()

with col3:
    if st.button("Multiplication"):
        st.success(f"Result = {num1 * num2}")
        st.balloons()

with col4:
    if st.button("Division"):
        if num2 != 0:
            st.success(f"Result = {num1 / num2}")
            st.balloons()
        else:
            st.error("Cannot divide by zero")