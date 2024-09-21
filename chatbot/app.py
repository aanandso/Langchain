from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 

import streamlit as st
import os

from dotenv import load_dotenv

os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

## prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a trivia expert. Please respond to the user queries."),
        ("user","Trivia Question: {question}")
    ]
)

## streamlit framework
st.title("LANGCHAIN DEMO")
input_text = st.text_input("Ask a question to a Trivia Expert")

## ollama llm = llama3.1:latest
llm = Ollama(model = "llama3.1:latest")

## output
output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))