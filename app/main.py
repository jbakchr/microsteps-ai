from fastapi import FastAPI
from app.schemas.request import GenerateRequest
from app.schemas.response import GenerateResponse
from app.ai.ollama_client import generate_microsteps

app = FastAPI()


@app.post("/generate-microsteps", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    steps = generate_microsteps(req.task)
    return GenerateResponse(microsteps=steps)