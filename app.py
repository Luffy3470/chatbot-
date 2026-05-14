from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv(".env")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

#prompt template and llm initialization
prompt = ChatPromptTemplate.from_template(
    "Answer the following question: {question}"
)
#model
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)
output_parser = StrOutputParser()
chain=prompt | llm | output_parser
st.title("AI Chatbot")

user_input = st.text_input("Ask something")

if user_input:
    response = llm.invoke(user_input)
    st.write(response.content)