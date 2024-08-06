import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

#Load the environment variable
load_dotenv()

#Page setting
st.set_page_config( page_title="Gemini-Chatbot!",
                   page_icon=":magnifying glass tilted left:",
                   layout="centered",#page layout
                   )

GoogleAPI_Key = os.getenv("GoogleAPI_Key")

#Gen AI Model
gen_ai.configure(api_key=GoogleAPI_Key)
model = gen_ai.GenerativeModel('gemini-pro')

def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role
    
    
#Intialize chat session

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history[])


#Chatbot title

st.title("Gemini - ChatBot")

#Display History
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)
        
        
#User input
user_input = st.chat_input("Ask Gemini...")

if user_input:
    st.chat_message("user").markdown(user_input) 
    
    gemini_response = st.session_state.chat_session.send_message(user_input)
    
    #Display Gemini Response
    
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)                 
