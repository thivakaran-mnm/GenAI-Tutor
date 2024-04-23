import streamlit as st
import google.generativeai as genai
import time

st.title("💬AI Data Science Tutor")

genai.configure(api_key='AIzaSyBQHsyjUUjsqzcL0vR_FHMKh-BfL2Vksx0')

model = genai.GenerativeModel(model_name='gemini-1.5-pro-latest',
                              system_instruction="""You are an AI Data Science Tutor, your name is ROBO-DSTutor. If a data science
                              topic is given as input help the user to understand it and if input query is not related to data science say you cannot answer in a humble way"""
                             )


if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello, How may I help you?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_query = st.chat_input()

if user_query is not None:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.write(user_query)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        ai_response = model.generate_content(user_query)
        st.write(ai_response.text)
    ai_message = {"role": "assistant", "content": ai_response.text}
    st.session_state.messages.append(ai_message)