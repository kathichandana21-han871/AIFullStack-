import streamlit as st
st.title("welcome to my first app")
st.write("Hello")
st.header("this is ai")
st.subheader("this is ur app")
st.chat_message("ask something")
st.chat_input("search..")
st.text_input("generate  image..")
name = st.text_input("Enter your name...")
if st.button("submit"):
    st.write("hello streamlit",name) 
