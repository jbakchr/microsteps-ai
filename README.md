# microsteps-ai

A simple local AI tool that helps reduce friction when starting tasks by generating small, actionable micro-steps.

---

## Goal (Current Focus)

The goal of this project is **not** to build a full productivity system.

Instead, the focus is to explore:

- How to generate _startable_ micro-steps
- Whether these steps actually reduce friction
- Whether they lead to **real-world action**

---

## Current Insight (Important)

The system is no longer just experimental — it has shown early signs of being genuinely useful.

Especially:

- A **very small first step** can be enough to trigger action
- Action does not need to be immediate — it can “stick” and happen later
- In some cases, even a single step can:
  - reduce resistance
  - create momentum
  - or lead to a feeling of **relief**

The goal is not to produce perfect plans — but to:

> ✅ help make *starting* feel easier

---

## Current Behavior

The system:

- Takes a task as input (e.g. `clean kitchen`)
- Uses a local AI model (via Ollama)
- Returns **3 micro-steps** designed as a small, coherent sequence

Example:

```

👉 Step 1: Pick up one dirty dish

Step 2: Put it in the sink
Step 3: Wipe down the counter beside it

```

---

## Important Learnings (So Far)

- ✅ Specific inputs → much better results  
  (`clean kitchen` > `clean apartment`)

- ✅ Steps work best when:
  - they are in the same context
  - they build on each other
  - they form a small “flow”

- ✅ Step 1 is the most important  
  → it should be extremely easy to start

- ✅ Steps 2–3 are often optional  
  → their role is to suggest continuation, not enforce it

---

## Feedback Loop (Core of This Project)

All real-world usage is tracked in:

👉 `FEEDBACK.md`

Each entry captures:

- Input
- Output
- Felt usefulness
- What actually happened (action or not)

---

## Why This Matters

The goal is not:

> “Did the output look good?”

But:

> ✅ “Did this help me move, think differently, or act — even later?”

---

## Current State

- ✅ Backend is stable (for now)
- ✅ CLI interface is simple but effective
- ✅ Output format supports action (Step 1 focus)
- ✅ Feedback loop is in active use

The project is now in a **usage and learning phase**, not a building phase.

---

## Requirements

- Python 3.11+
- Ollama running locally

---

## Install

```bash
pip install -r requirements.txt
```

***

## Run

```bash
uvicorn app.main:app --reload
```

***

## CLI Usage

```bash
python test_cli.py
```

***

## Notes (Current Direction)

*   No persistence
*   No memory system
*   No complex frontend

This is intentional.

The focus remains:

> ✅ understanding what actually helps in real-life situations

***

## Possible Future Directions

(Not prioritized — will depend on continued usage)

*   Better input guidance
*   Lightweight UI / frontend
*   Modes (start vs execute)
*   Improvements based on feedback patterns

***

## License

MIT

