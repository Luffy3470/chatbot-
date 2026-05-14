# AI Chatbot using LangChain, Groq, and Ollama

A simple AI chatbot built using:

- LangChain
- Groq API
- Ollama
- Streamlit
- Python

This project supports both:
- Cloud-based LLM inference using Groq
- Local LLM inference using Ollama

---

# Features

- Real-time AI chatbot
- LangChain integration
- Streamlit web interface
- Secure API key handling using `.env`
- Groq cloud inference support
- Ollama local inference support
- Prompt templates and output parsing

---

# Tech Stack

- Python
- LangChain
- Groq API
- Ollama
- Streamlit
- python-dotenv

---

# Project Structure

```text
Chatbot/
│
├── app.py
├── locallamma.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repository-link>
cd Chatbot
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
venv\Scripts\activate.bat
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
LANGCHAIN_API_KEY=your_langchain_key
```

---

# Run Groq Cloud Chatbot

```bash
streamlit run app.py
```

Model used:
- `llama-3.1-8b-instant`

---

# Run Local Ollama Chatbot

## Download Ollama Model

```bash
ollama pull llama3
```

## Run Local Chatbot

```bash
streamlit run locallamma.py
```

Local model used:
- `llama3`

---

# Future Improvements

- Chat history
- Streaming responses
- RAG pipeline
- PDF Q&A system
- Vector database integration
- Multi-model support
- Agent workflows

---

# Author

Roshan Bhaskar
