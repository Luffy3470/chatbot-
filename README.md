# AI Chatbot using LangChain and Groq

A simple AI chatbot built using:

- LangChain
- Groq API
- Streamlit
- Python

This project uses the Groq inference API with the Llama 3.1 model to generate real-time AI responses through a Streamlit interface.

---

## Features

- Real-time AI chatbot
- LangChain integration
- Secure API key management using `.env`
- Simple Streamlit web interface
- Fast responses using Groq inference

---

## Tech Stack

- Python
- LangChain
- Groq API
- Streamlit
- python-dotenv

---

## Project Structure

```text
Chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd Chatbot
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

#### Windows CMD

```cmd
venv\Scripts\activate.bat
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Setup Environment Variables

Create a `.env` file in the project folder:

```env
GROQ_API_KEY=your_api_key
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Model Used

- `llama-3.1-8b-instant`

Powered by Groq inference.

---

## Future Improvements

- Chat history
- Streaming responses
- PDF Q&A
- RAG pipeline
- Vector database integration
- Multi-model support

---

## Author

Roshan Bhaskar
