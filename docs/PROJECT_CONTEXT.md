# microsteps-ai – Project Context

## 🧠 What this project is

microsteps-ai is a simple, local AI tool that helps reduce friction when starting tasks by generating small, actionable micro-steps.

The focus is NOT productivity, planning, or task management.

The focus is:
> Helping initiate action in the real world.

---

## 🎯 Core philosophy

The goal is not:
- to generate “good” steps  
- to optimize task completion  

The goal is:
> to generate steps that actually make me start

Success is measured by:
- Did I act?
- Did it feel easy to start?

---

## 🧪 Current state

The system currently works as:

```

input → generate steps → manual reflection

```

Key characteristics:
- Works best with specific inputs (e.g. "clean kitchen")
- Struggles with broad inputs (e.g. "clean apartment")
- Feedback is manually logged in FEEDBACK.md
- Focus is experimental and behavior-driven

---

## 🔍 Key insight so far

The main bottleneck is:
> Input quality and step “startability”

Good outputs depend heavily on:
- how concrete the input is
- how small and physical the steps feel

---

## 🧭 Intended direction (high level)

The project may evolve into a more structured system:

```

input → refine → generate → interact → feedback → learn

```

The intention is NOT to make it complex, but to:
- reduce friction
- improve usefulness
- learn from real usage

---

## 🧱 Near-term evolution ideas

### 1. Input refinement
- detect vague inputs
- suggest narrower starting points
- guide the user toward something startable

---

### 2. Mode-based generation
- start mode → small activation steps (default)
- low-energy mode → extremely easy steps
- execution mode → slightly more productive steps

---

### 3. Structured feedback
- automatic logging (instead of manual)
- simple structured format (JSON-like)
- easier to analyze patterns over time

---

## 🔄 Structural shift (important)

From:

```

input → LLM → output

```

To:

```

input → refine → generate → interact → feedback → store

```

This is the transition from:
> a script  

to:
> a simple system

---

## 🚫 Non-goals

- Not a full productivity system
- Not a generic AI framework
- Not feature-heavy or complex
- Not optimized for scale

---

## ✅ What makes this project different

This is not:
- a chatbot
- a summarizer
- a productivity app

This is:
> a behavior-focused tool

It aims to:
- reduce mental friction
- help initiate action
- learn from real-world usage

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

- Evolving this into a structured but still simple system
- Keeping it minimal and practical (avoid overengineering)
- Learning real AI engineering patterns (not just tools)
- Iterating step-by-step based on real usage


***

# 💡 How to use it

When you start a new chat, you can simply do:

```text
I’m working on this project:

[paste PROJECT_CONTEXT.md]

I want help evolving it step-by-step without overengineering. Let’s start with [X].
```


