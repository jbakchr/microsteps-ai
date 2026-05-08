import requests
from app.ai.prompt_builder import build_prompt
from app.ai.parser import parse_steps

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def generate_microsteps(task: str):
    prompt = build_prompt(task)

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    text = data.get("response", "")

    return parse_steps(text)