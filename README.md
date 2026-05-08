# microsteps-ai

A simple local AI tool that helps reduce friction when starting tasks by generating small, actionable micro-steps.

---

## Goal (Current Focus)

The goal of this project is **not** to build a full productivity system.

Instead, the focus is to explore:

- How to generate _startable_ micro-steps
- Whether these steps actually reduce friction
- Whether they lead to **real-world action**

This project is currently in an **experimental phase**, where the main purpose is to learn what works (and what doesn’t).

---

## Current Behavior

The system:

- Takes a task as input (e.g. `clean kitchen`)
- Uses a local AI model (via Ollama)
- Returns **a small number of micro-steps** designed to help start the task

Example:

```

Input:
clean kitchen

Output:

*   Go to kitchen and look at counter
*   Pick up items from one small area
*   Put them in sink or trash

```

---

## Important Insight (So Far)

The quality of the output depends heavily on the **input**.

Better results come from:

- ✅ Specific inputs: `clean kitchen`, `clean desk`
- ❌ Broad inputs: `clean apartment`

For now, the system works best when the task is already **narrow and concrete**.

---

## Feedback Loop (Core of This Project)

A key part of this project is manually tracking how the system performs in real life.

All usage is logged in:

👉 `FEEDBACK.md`

Each entry captures:

- Input (what was asked)
- Output (what the model suggested)
- Felt quality (good / okay / bad)
- Actual behavior (did I act or not)

---

## Why This Matters

The goal is not:

> "Do the steps look good?"

But:

> ✅ "Did this help me _start_ something?"

This feedback loop helps identify:

- Which types of inputs work best
- What makes steps feel _startable_
- When suggestions lead to action (or not)

---

## Requirements

- Python 3.11+
- Ollama running locally

---

## Install

```bash
pip install -r requirements.txt
```

---

## Run

```bash
uvicorn app.main:app --reload
```

---

## Test (API)

```bash
curl -X POST http://localhost:8000/generate-microsteps \
  -H "Content-Type: application/json" \
  -d '{"task": "clean kitchen"}'
```

---

## Simple CLI Test

```bash
python test_cli.py
```

---

## Notes (Current State)

- No persistence (by design)
- No frontend (yet)
- No memory or personalization
- Focus is purely on generating micro-steps

This is intentional to keep the project simple and focused.

---

## Possible Future Directions

(Not prioritized yet — depends on feedback and learning)

- CLI improvements
- Desktop quick-capture tool
- Guided input (help narrow broad tasks)
- Task “start mode” vs “execute mode”
- Smarter prompts based on feedback patterns

---

## License

MIT
