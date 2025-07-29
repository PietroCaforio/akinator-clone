from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
from backend.model_utils import get_question, go_to_next_node, get_prediction
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Keep sessions in memory (replace with DB or JWT later)
session_state = {}

class AnswerRequest(BaseModel):
    session_id: str
    answer_yes: bool

@app.get("/start_game")
def start_game(session_id: str):
    session_state[session_id] = 0  # root node
    question = get_question(0)
    return {"question": question}

@app.post("/answer")
def answer(req: AnswerRequest):
    node = session_state.get(req.session_id, 0)
    next_node = go_to_next_node(node, req.answer_yes)
    session_state[req.session_id] = next_node

    question = get_question(next_node)
    if question:
        return {"question": question}
    else:
        guess = get_prediction(next_node)
        return {"guess": guess}
