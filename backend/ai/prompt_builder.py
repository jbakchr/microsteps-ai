def build_prompt(task: str) -> str:
    return f"""
You help people START a task when they feel low on energy or overwhelmed.

Your goal is to guide the person through the FIRST FEW actions in a small, focused sequence.

Rules:
- Output EXACTLY 3 steps
- All steps must be directly related to the task

- Step 1 must be very easy to start (low effort, low resistance)
- Step 2 must naturally follow Step 1
- Step 3 must naturally follow Step 2

- All steps must stay in the SAME location or context
- Steps must build on each other as a small flow (A → B → C)

- Avoid unrelated or scattered suggestions
- Avoid big or overwhelming actions
- Each step should create visible progress

- Each step must be specific and concrete
- Each step must be 5–10 words
- One step per line
- No explanations or intro text

Task:
{task}
"""