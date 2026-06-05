# microsteps-ai – Roadmap

This document captures potential future directions for the project.

The purpose is **not to commit to building features**,  
but to guide **what to explore next based on real-world usage**.

---

## 🧭 Current Phase: Usage + Behavior Learning

The project is currently in a:

> ✅ **stabilization and learning phase**

Focus:

- Use the tool in real-life situations
- Maintain consistent usage
- Protect and reinforce the “start → act” behavior loop
- Continue logging in `FEEDBACK.md`

---

## 🔥 Most Important Insight Right Now

The biggest risk is no longer:

❌ Bad outputs

The biggest risk is:

> ❗ **Not using the tool at all**

Because:

- The tool already works well enough
- It already triggers action
- But usage depends heavily on **availability and access**

---

## ⚡ Priority: Reduce Access Friction

Before improving intelligence:

> ✅ Ensure the tool is always easy to use

Current direction:

- ✅ Global CLI (`microsteps`)
- ✅ Fast interaction loop
- ✅ Minimal startup friction

---

## 🧱 Next Evolution Steps (In Order)

### 1. Input Refinement (Next Step)

Problem:

- Broad inputs → weak outputs

Goal:

- Help the user start with something concrete

Approach:

- Detect vague inputs
- Suggest 2–3 narrower starting points
- Keep interaction lightweight

Important:

- Do not over-engineer
- Do not build a full system
- Keep it fast and optional

---

### 2. Output Improvement (Later)

Goal:

- Increase “startability” of steps

Possible directions:

- Stronger emphasis on Step 1
- Better phrasing of steps
- More physical / immediate actions

Important:

- Evaluate only based on real-world action
- Not based on “how good it looks”

---

### 3. Interaction Loop (Later)

Current:

```

input → output

```

Possible evolution:

```

input → refine → generate → user reacts

```

Examples:

- Ask one clarifying question
- Allow simple follow-up interaction

Important:

- Must reduce friction, not increase it

---

### 4. Modes (Later)

Problem:

- Different situations require different types of steps

Possible modes:

- **Start mode** → very small steps (default)
- **Low-energy mode** → extremely easy steps
- **Execution mode** → slightly more progress-oriented

Important:

- Only introduce if real need is observed
- Avoid adding complexity too early

---

### 5. Feedback Structuring (Later)

Current:

- Manual logging in `FEEDBACK.md`

Possible:

- Lightweight structured feedback (JSON-like)

Goal:

- Identify patterns over time

Important:

- Do not sacrifice reflection quality
- Keep friction low

---

### 6. Lightweight UI (Optional / Later)

Purpose:

- Make the tool more “present” and easier to access

Options:

- small desktop UI
- minimal browser interface

Important:

- Only if CLI becomes limiting
- Must remain fast and simple

---

## 🚫 What NOT to Do (Very Important)

- ❌ No database / persistence (for now)
- ❌ No complex architecture
- ❌ No memory / RAG systems
- ❌ No feature-heavy design
- ❌ No “product thinking” over behavior thinking

---

## 🧠 Guiding Principle

This is not a feature-building project.

It is a learning process:

> ✅ What actually helps me start doing things?

Everything else is secondary.

---

## 🔑 Core Constraint

Every change must answer:

- Did this reduce friction?
- Did this help me act faster?
- Did this make starting easier?

If not:

👉 Do not build it
