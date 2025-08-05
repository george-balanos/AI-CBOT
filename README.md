# AI‑CBOT 🤖

An AI-powered chatbot app built with **FastAPI backend**, **React frontend**, **LangChain + Ollama**, and **SQLite** message persistence. ⚙️

---

## Features

- User login and unique username validation  
- Chat interface using React  
- Conversation history stored in SQLite  
- AI responses powered by Ollama LLM via LangChain

  ## 🧱 Project Structure
  backend/
  ├── backend_api/
  │ └── handlers.py # FastAPI endpoints
  ├── database_utils.py # SQLite helpers
  └── requirements.txt
  
  frontend/
  └── React app (WelcomePage & ChatBoard)

  ## 🚀 Quick Start

  ### 1. Backend (FastAPI + SQLite)
  
  ```bash
  cd backend
  pip install -r requirements.txt
  python database_utils.py   # Initializes the database
  uvicorn backend.backend_api.handlers:app --reload # This runs your API at http://localhost:8000
  ```

  ### 2.Frontend (React)
  ```bash
  cd frontend/chatbot-frontend
  npm install
  npm start
  ```

  ## 🗂️ Database Schema (SQLite)
  ```bash
  CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE
  );
  
  CREATE TABLE user_message_history (
    message_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    sender TEXT NOT NULL, -- 'human' or 'system'
    message TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE
  );
  ```
  * users: Stores unique usernames.
  * user_message_history: Tracks all chat messages linked to users, with timestamps and sender info.
