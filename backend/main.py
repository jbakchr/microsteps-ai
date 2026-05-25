from fastapi import FastAPI
from backend.schemas.request import GenerateRequest
from backend.schemas.response import GenerateResponse
from backend.ai.ollama_client import generate_microsteps

app = FastAPI()


@app.post("/generate-microsteps", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    steps = generate_microsteps(req.task)
    return GenerateResponse(microsteps=steps)