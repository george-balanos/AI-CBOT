from ..llm import generator
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

class QueryData(BaseModel):
    text: str = Field(..., min_length=1)

app = FastAPI()

all_queries = {}

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