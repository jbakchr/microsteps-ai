# microsteps/core/generate.py

import ollama

def generate_microsteps(task: str) -> list[str]:
    prompt = f"""
Break this into 3 very small, physical steps that are easy to start.

Task: {task}

Rules:
- Step 1 must be extremely easy
- Focus on physical actions
- Avoid thinking/planning steps

Output format:
Step 1: ...
Step 2: ...
Step 3: ...
"""

    response = ollama.chat(
        model="llama3",
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    text = response["message"]["content"]

    # simple parsing (keep minimal)
    steps = [line.strip() for line in text.split("\n") if line.strip()]
    return steps[:3]