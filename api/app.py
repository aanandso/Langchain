from fastapi import FastAPI

from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

from langserve import add_routes

import uvicorn
import os

from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

## ollama llm = llama3.1:latest
llm = Ollama(model = "llama3.1:latest")

prompt1 = ChatPromptTemplate.from_template(
    "Create an essay on {topic} with 100 words"
)

prompt2 = ChatPromptTemplate.from_template(
    "Create an poem on {topic} with 100 words"
)

add_routes(
    app,
    prompt1|llm,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if  __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)
