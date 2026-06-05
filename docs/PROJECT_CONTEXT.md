# microsteps-ai – Project Context

---

## 🧠 What this project is

microsteps-ai is a simple, local AI CLI tool that helps reduce friction when starting tasks by generating small, actionable micro-steps.

The focus is NOT productivity, planning, or task management.

The focus is:

✅ Helping initiate action in the real world

---

## 🎯 Core philosophy

The goal is not:

- to generate “good” steps
- to optimize task completion

The goal is:

> ✅ to generate steps that actually make me start

Success is measured by:

- Did I act?
- Did it feel easy to start?

---

## ⚡ Key realization (important)

The system already works.

The biggest risk is no longer:

❌ “bad outputs”

The biggest risk is:

> ❗ Not using the tool

Because:

- The tool can already trigger action
- But only if it is **easy and fast to access**

---

## 🔁 Current behavior loop

What actually happens in practice:

```

trigger → run tool → act

```

The tool is becoming:

> ✅ A behavior trigger (not just a generator)

---

## 🧪 Current state

The system currently works as:

```

input → generate → act → manual reflection

```

Key characteristics:

- Works best with specific inputs (e.g. "clean kitchen")
- Struggles with broad inputs (e.g. "clean apartment")
- CLI is globally available (`microsteps`)
- No backend or server required
- Core logic runs locally and calls Ollama directly
- Feedback is logged in `FEEDBACK.md`
- Focus is experimental and behavior-driven

---

## 🏗️ Current architecture (important)

```

CLI → core logic → AI model (Ollama)

```

Principles:

- CLI is intentionally **simple and “dumb”**
- Core contains **behavior + generation logic**
- No network layer / no backend server
- System is local-first, fast, and always available

---

## 🔍 Key insights so far

- ✅ Specific inputs → much better results
- ✅ Step 1 is the most important
- ✅ Small, physical steps work best
- ✅ Action can happen immediately OR later
- ✅ The tool works even with imperfect outputs
- ✅ Availability and ease-of-use are critical

---

## 🧭 Intended direction (high level)

The system may evolve into:

```

input → refine → generate → (light interaction) → feedback

```

But:

> ❗ This must remain simple

The goal is NOT to build a complex system, but to:

- reduce friction
- improve usefulness
- reinforce real-world action

---

## 🧱 Near-term evolution priorities

### 1. Protect usage (highest priority)

- Keep access friction near zero
- Maintain instant CLI usage
- Avoid anything that slows down interaction

---

### 2. Input refinement (next step)

- Detect vague inputs
- Suggest narrower starting points
- Guide toward something startable

Important:

- Must remain fast and optional
- Must NOT become a multi-step interaction

---

### 3. Step 1 quality (highest leverage)

- Make Step 1 extremely easy
- Focus on physical actions
- Reduce thinking required
- Aim for <10-second start

---

## 🔄 Structural shift (important)

From:

```

input → LLM → output

```

To:

```

trigger → microstep → action

```

This is the shift from:

> a tool that generates steps

to:

> ✅ a system that triggers behavior

---

## 🚫 Non-goals

- Not a full productivity system
- Not a generic AI framework
- Not feature-heavy or complex
- Not optimized for scale
- Not dependent on external services or infrastructure

---

## ✅ What makes this project different

This is not:

- a chatbot
- a summarizer
- a productivity app

This is:

> ✅ a behavior-focused tool

It aims to:

- reduce mental friction
- help initiate action
- reinforce useful habits

---

## 🧠 Why this matters (personally)

This project is useful for:

- executive function challenges
- difficulty starting tasks
- reducing overwhelm

It is both:

- a technical experiment
- a personal support tool

---

## 🚀 What I want help with in a new chat

- Evolving this into a simple but structured system
- Keeping it minimal and practical (avoid overengineering)
- Designing behavior-first improvements (not feature-first)
- Iterating step-by-step based on real usage

---

## 💡 How to use this context

When starting a new chat, you can say:

```

I’m working on this project:

\[paste PROJECT\_CONTEXT.md]

I want help evolving it step-by-step without overengineering.
Let’s start with \[X].

```
