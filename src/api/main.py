from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.services.ai_service import ask_gpt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    prompt: str

@app.post("/ask")
async def ask_question(user_input: UserInput):
    try:
        response = await ask_gpt(user_input.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    