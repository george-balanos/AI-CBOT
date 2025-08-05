# AI‑CBOT 🤖

An AI-powered chatbot app built with **FastAPI backend**, **React frontend**, **LangChain + Ollama**, and **SQLite** message persistence. ⚙️

---



https://github.com/user-attachments/assets/5cc11d04-95a6-4202-a29a-c53fe92aa5df



## Features

- User login and unique username validation  
- Chat interface using React  
- Conversation history stored in SQLite  
- AI responses powered by Ollama LLM via LangChain

  ## 🧱 Project Structure
  backend/ <br>
  ├ backend_api/ <br>
  │ └ handlers.py # FastAPI endpoints <br>
  ├ database_utils.py # SQLite helpers <br>
  └ requirements.txt <br>
  
  frontend/ <br>
  └ React app (WelcomePage & ChatBoard)

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
