import ollama

def generate_microsteps(task: str) -> list[str]:
    

    prompt = f"""
You generate micro-steps to help someone START a task immediately.

STRICT RULES:
- Output EXACTLY 3 steps
- Each step must be ONE short sentence
- NO explanations
- NO introductions
- NO commentary
- NO extra text before or after
- Step 1 MUST be extremely easy (almost trivial)
- Each step must describe a PHYSICAL action

BAD OUTPUT (DO NOT DO THIS):
"Here are some steps to help..."
"To get started, you can..."
"Start by thinking about..."

GOOD OUTPUT (DO THIS FORMAT ONLY):
Step 1: Pick up one item from the floor
Step 2: Put it away
Step 3: Stand still and look around the room

TASK:
{task}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response["message"]["content"]

    steps = [
        line.strip()
        for line in text.split("\n")
        if line.strip().startswith("Step")
    ]

    return steps[:3]