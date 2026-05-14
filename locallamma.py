import streamlit as st
from dotenv import load_dotenv

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv(".env")

# Prompt template
prompt = ChatPromptTemplate.from_template(
    "Answer the following question: {question}"
)

# Local Ollama model
llm = Ollama(
    model="llama3"
)

# Output parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

# Streamlit UI
st.title("AI Chatbot")

user_input = st.text_input("Ask something")

if user_input:
    response = chain.invoke({
        "question": user_input
    })

    st.write(response)