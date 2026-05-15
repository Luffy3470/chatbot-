from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv(".env")

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Memory initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Prompt
prompt = ChatPromptTemplate.from_template(
    """
    Conversation history:
    {history}

    User: {question}
    """
)

# Model
llm = ChatGroq(
    model_name="llama-3.1-8b-instant"
)

# Parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

# UI
st.title("AI Chatbot")

user_input = st.text_input("Ask something")

if user_input:

    # Convert memory into text
    history = "\n".join(st.session_state.messages)

    # Invoke chain
    response = chain.invoke({
        "history": history,
        "question": user_input
    })

    # Store conversation
    st.session_state.messages.append(f"User: {user_input}")
    st.session_state.messages.append(f"AI: {response}")

    # Display response
    st.write(response)