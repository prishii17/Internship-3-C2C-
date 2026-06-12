import streamlit as st

st.title("Example 1")
no = st.text_input("Enter No")
if(st.button("Clickme")):
    if int(no) %2==0:
        st.write("Ans is:")
        st.success("No is Even")
        st.balloons()
else:
    st.write("Ans is")
    st.warning("No is Odd ")