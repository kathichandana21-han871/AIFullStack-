import ollama
import streamlit as st
st.title("UIBOT!!")
with st.sidebar:
    personalities={
        "Kid": " Give the answers like you are explaining to a 5 years old kid. Give the answer in 2 lines only ",
        "Proffesor": "You are an IIT professor.Explain the topics using correct terminology.Give the answer"
    }
    personality = st.selectbox("Select a personality",personalities.keys())
    if st.button("Clear Chat"):
        st.session_state.message=[]
        st.success("Chat cleared successfully")
        
    uploaded_file=st.file_uploader("upload a file...")
    if uploaded_file:
        st.write("File uploaded successfully...")
        with st.expander("preview"):
            context=uploaded_file.read().decode("utf-8")
            st.text(context)
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("You : ")
if question:
    with st.chat_message("User"):
        st.write("User: ",question)
    
    st.session_state.messages.append(
        {
            "role" : "user",
            "content" : question
        }
    )
    with st.spinner("Thinking......"):
        response = ollama.chat(
            model="llama3.2:3b",
            messages =[{
                "role": "system", "content": "Give answer in 2 lines only"
            }]+st.session_state.messages)
    st.session_state.messages.append(
            {
                "role" : "assistant",
                "content":response["message"]["content"]
            }
        )
    with st.chat_message("Assistant"):
        st.write("AI:",response["message"]["content"])
