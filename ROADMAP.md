# microsteps-ai – Roadmap

This document outlines **what to explore next based on real-world usage**.

This is NOT a feature roadmap.

It is a guide for:

> ✅ what actually improves real-world action

---

## 🧭 Current Phase: Usage + Behavior Learning

The project is in a:

✅ **usage-first phase**

Focus:

- Use the tool in real situations
- Maintain frequent usage
- Strengthen the “trigger → act” loop
- Log real experiences in `FEEDBACK.md`

---

## 🔥 Most Important Insight

The biggest risk is NOT:

❌ bad outputs

The biggest risk is:

> ❗ **not using the tool at all**

Because:

- The system already works
- It already triggers action
- But only if it is instantly accessible

---

## ⚡ Priority #1: Protect Usage

Before improving intelligence:

> ✅ ensure the tool is always used

Current state:

- ✅ Global CLI (`microsteps`)
- ✅ No backend / no startup step
- ✅ Instant execution
- ✅ Minimal friction

---

## 🧱 Current Architecture

```

CLI → core logic → Ollama

```

Principles:

- ✅ No backend server
- ✅ No network layer
- ✅ Local, fast, always available
- ✅ CLI is simple and “dumb”
- ✅ Core handles behavior logic

---

## 🧠 Key Constraints

Every change must answer:

- Did this reduce friction?
- Did this make it easier to start?
- Did I use the tool more?

If not:

> ❌ do not build it

---

## 🧱 Next Evolution Steps (in order)

---

### 1️⃣ Input Refinement (Next step)

Problem:

- Broad inputs → weak outputs
- Example: “clean apartment”

Goal:

> ✅ help the user start from something concrete

Approach:

- Detect vague inputs
- Suggest 2–3 smaller starting points
- Keep interaction **optional and minimal**

Important:

- ❌ no heavy interaction
- ❌ no multi-step flows
- ✅ must feel instant

---

### 2️⃣ Improve Step 1 Quality (High leverage)

Goal:

> ✅ make Step 1 almost impossible NOT to do

Focus:

- extremely small actions
- physical actions only
- <10 second effort
- zero thinking required

Examples:

- ✅ “Pick up one item”
- ❌ “Start organizing the kitchen”

Important:

- Evaluate based on:
  - Did I act immediately?
  - Did it feel easy?

---

### 3️⃣ Optional Argument Input (Low friction gain)

Allow:

```bash
microsteps clean kitchen
```

Instead of:

```
run → type → enter
```

Goal:

> ✅ reduce friction from 2 steps → 1 step

---

### 4️⃣ Lightweight Interaction (Only if needed)

Possible:

```
input → refine → confirm → generate
```

Examples:

- “Do you want to start with dishes, counter, or trash?”

Important:

- ❗ must not slow down usage
- ❗ must be skippable
- ❗ must feel faster, not smarter

---

### 5️⃣ Mode System (Only if real need appears)

Possible modes:

- **Start mode (default)** → very small steps
- **Low-energy mode** → extremely easy actions
- **Execution mode** → slightly more progress-oriented

Important:

- ❌ do not add unless clearly needed
- ❌ avoid complexity

---

### 6️⃣ Feedback Structuring (Optional)

Current:

- manual logging in `FEEDBACK.md`

Possible:

- lightweight structured format (JSON-like)

Goal:

- detect patterns over time

Important:

- ✅ keep reflection quality
- ❌ do not add friction

---

## 🚫 What NOT to Do (Very Important)

- ❌ No backend / API layer
- ❌ No database / persistence (for now)
- ❌ No complex architecture
- ❌ No RAG / memory systems
- ❌ No feature-heavy design
- ❌ No “product thinking”

---

## 🧠 Guiding Principle

This is not a feature-building project.

It is an experiment:

> ✅ What actually helps me start doing things?

Everything else is secondary.

---

## 🔑 Final Constraint

The system must feel like:

> ✅ a reflex

Not:

> ❌ a tool that requires setup

---

## 🧭 Direction Summary

From:

```
input → LLM → output
```

To:

```
trigger → microstep → action
```

This is the shift from:

> ❌ generating steps

to:

> ✅ enabling behavior
