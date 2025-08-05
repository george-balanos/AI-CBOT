from ..llm import generator
from fastapi import FastAPI, HTTPException, Request, Query
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

from .helpers import login_user, get_all_user_messages, add_message

class QueryData(BaseModel):
    text: str = Field(..., min_length=1)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
async def login(request: Request):
    data = await request.json()

    username = data["username"]
    print("Received username: ", username)

    login_user(username)

    return {
        "username": username,
        "message": f"Welcome, {username}"
    }

@app.get("/chat/messages")
async def get_messages(username: str = Query(...)):
    print("Sending message history of user:", username)
    message_history = get_all_user_messages(username)
    print(message_history)
    return {"messages": message_history}

@app.post("/chat/query")
async def answer_query(request: Request):
    data = await request.json()
    print(f"Received user question: {data['user_question']}")
    add_message(data["username"], data["user_question"], "human")

    messages = get_all_user_messages(data["username"])
    message_history = convert_messages_to_history(messages)
    print(message_history)

    chatbot_response, updated_history = generator.generate_answer(message_history, data["user_question"])
    print(f"System: {chatbot_response}")

    add_message(data["username"], chatbot_response, "system")

    return {"response": chatbot_response}

def convert_messages_to_history(messages):
    msg_history = []
    for msg in messages:
        msg_history.append((msg["sender"], msg["message"]))
    return msg_history