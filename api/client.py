import requests
import streamlit as st

def get_prompt1_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']


def get_prompt2_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']


## streamlit framework
st.title("Langchain DEMO")

input_text_essay = st.text_input("Write an essay on ", key="essay_input")
input_text_poem = st.text_input("Write an essay on ", key="text_input")

if input_text_essay:
    st.write(get_prompt1_response(input_text_essay))

if input_text_poem:
    st.write(get_prompt2_response(input_text_poem))