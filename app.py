from dotenv import load_dotenv
load_dotenv() ## loading all environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## func to load gemini and get responses
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

##streamlit
st.set_page_config(page_title="QnA Demo")
st.header("Gemini LLM application")

input=st.text_input("Input: ",key='input')
submit = st.button('Ask the question')

##When submit clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The Reasponse is")
    st.write(response)