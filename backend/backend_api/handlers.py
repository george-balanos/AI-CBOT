from ..llm import generator
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

class QueryData(BaseModel):
    text: str = Field(..., min_length=1)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

all_queries = {}

@app.post("/login")
async def login(request: Request):
    data = await request.json()
    print("Received username: ", data["username"])
    return {"message": f"Welcome, {data['username']}"}

@app.put("/query/{user_id}")
def execute_query(user_id: str, query_data: QueryData):

    text = query_data.text

    message_history = all_queries.get(user_id, [("system", "You are a helpful AI chat bot. Your name is AI-CBOT!")])

    try:
        response, updated_message_history = generator.generate_answer(message_history, text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    all_queries[user_id] = updated_message_history

    return {
        "user_id": user_id,
        "input_text": text,
        "response": response,
        "message_history": updated_message_history
    }

@app.get("/messages")
def get_message_history():
    return all_queries