# AI Chatbot using LangChain + Groq + Streamlit

A conversational AI chatbot built using LangChain, Groq, and Streamlit with conversation memory support.

## Features

* Conversational AI chatbot
* Memory-based chat history
* Built using LangChain Expression Language (LCEL)
* Fast inference using Groq API
* Streamlit web interface
* Environment variable support using `.env`
* LangSmith tracing support

---

# Tech Stack

* Python
* LangChain
* Groq API
* Streamlit
* python-dotenv

---

# Project Structure

```bash
AI-Chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Installation

## 1. Clone the repository

```bash
git clone <your-repo-url>
cd AI-Chatbot
```

---

## 2. Create virtual environment

### Windows

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# How It Works

The chatbot follows this pipeline:

```text
User Input
   ↓
Prompt Template
   ↓
Groq LLM
   ↓
Output Parser
   ↓
Response Display
```

Conversation history is stored using Streamlit session state and passed back into the prompt for contextual memory.

---

# Memory Implementation

Chat history is stored using:

```python
st.session_state.messages
```

Previous messages are injected into the prompt template to create conversational context.

---

# LangChain Components Used

## ChatPromptTemplate

Used to dynamically create prompts.

## ChatGroq

Connects the application to Groq-hosted LLMs.

## StrOutputParser

Converts model responses into plain strings.

## LCEL Chain

```python
chain = prompt | llm | output_parser
```

Creates a LangChain execution pipeline.

---

# Example Prompt Flow

```text
Conversation history:
User: Hello
AI: Hi! How can I help you?

User: What is Machine Learning?
```

---

# Future Improvements

* Chat UI with message bubbles
* Streaming responses
* Multiple LLM support
* RAG integration
* PDF chatbot
* Database memory
* Authentication system
* Deployment on Streamlit Cloud or Render

---

# Requirements

Example `requirements.txt`

```txt
langchain
langchain-groq
streamlit
python-dotenv
```

---

# Important Notes

Do NOT upload:

* `.env`
* API keys
* virtual environment folders

Use `.gitignore`:

```txt
venv/
.env
__pycache__/
```

---

# Author

Roshan Bhaskar
B.Tech Civil Engineering, National Institute of Technology Tiruchirappalli
AI/ML Enthusiast | LLM Engineering | Full Stack Development
