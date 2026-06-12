import streamlit as st

st.title("Welcome to Calculator")

st.write("enter choice of operation")
st.write("1. Addition")
st.write("2. Subtraction")
st.write("3. Multiplication")
st.write("4. Division")

opp = st.number_input("enter the choice")

num1 = st.number_input("enter first number")
num2 = st.number_input("enter second number")

if st.button("submit"):
    if opp == 1:
        st.write("result is ", num1 + num2)
    elif opp == 2:
        st.write("result is ", num1 - num2)
    elif opp == 3:
        st.write("result is ", num1 * num2)
    elif opp == 4:
        if num2 != 0:
            st.write("result is ", num1 / num2)
        else:
            st.error("cannot divide by zero")
    else:
        st.error("invalid choice")
st.balloons()
    
