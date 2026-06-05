# microsteps-ai

A simple, local AI tool that helps reduce friction when starting tasks by generating small, actionable micro-steps.

---

## 🧠 Purpose

This project is **not** about productivity or planning.

It is about:

> ✅ Helping initiate action in the real world

The goal is not:
- to generate “perfect” steps  
- to optimize completion  

The goal is:

> ✅ To make starting feel easy

---

## 🎯 Success Criteria

The system is successful if:

- ✅ You start doing something  
- ✅ The first step feels easy  
- ✅ Resistance is reduced  

---

## ⚙️ How It Works

The current system follows a simple loop:

```

input → generate → act → reflect

```

- You provide a task (e.g. “clean kitchen”)
- The system generates **3 small micro-steps**
- You act immediately (ideally without overthinking)

---

## ✅ Example Output

```

👉 Step 1: Pick up one dirty dish

Step 2: Put it in the sink
Step 3: Wipe down the counter beside it

```

---

## 🧠 Key Learnings So Far

- ✅ **Specific inputs → much better outputs**
  - "clean kitchen" > "clean apartment"

- ✅ **Step 1 is everything**
  - It should feel almost too easy

- ✅ **Momentum matters more than structure**
  - Steps 2–3 are optional

- ✅ Even small actions can:
  - reduce resistance  
  - create momentum  
  - lead to delayed action  

---

## 📦 Project Structure

```

backend/          → AI + logic ("the brain")
interfaces/
cli/           → command-line interface
streamlit/     → optional UI interface (future/experimental)
docs/            → context, feedback, evolution

```

---

## 🚀 Setup

### Requirements

- Python 3.11+
- Ollama running locally

---

### Install

```bash
pip install -r requirements.txt
````

***

### Install CLI (global command)

From project root:

```bash
pip install -e .
```

This makes the CLI available globally:

```bash
microsteps
```

***

## ⚡ Usage

### 1. Start backend

```bash
uvicorn backend.main:app --reload --port 8006
```

***

### 2. Run CLI (from anywhere)

```bash
microsteps
```

***

### 3. Typical flow

* Open terminal
* Run `microsteps`
* Enter task
* Start acting immediately

***

## 🧠 Architecture Principles

* ✅ Backend = **behavior + logic**
* ✅ CLI = **simple interface**
* ✅ System = minimal, local, fast

The CLI should stay **dumb and frictionless**  
The backend may evolve (refinement, modes, etc.)

***

## 🧪 Feedback Loop

All real-world usage is tracked in:

```
docs/FEEDBACK.md
```

Each entry captures:

* Input
* Output
* Whether you acted
* How it felt

***

## 🧭 Current Phase

The project is in a:

> ✅ **Usage + learning phase**

Not a feature-building phase.

Focus is on:

* What actually helps you start
* What reduces friction
* What creates real-world action

***

## 🔮 Possible Future Directions

(Not prioritized — only if supported by real usage)

* Input refinement (handle vague tasks)
* Different modes (low-energy, execution)
* Structured feedback (lightweight)
* Simple UI for faster access

***

## 🚫 Non-Goals

* Not a productivity system
* Not a task manager
* Not a complex AI framework
* Not optimized for scale

***

## 🧠 Core Idea

This is not just a tool.

It is:

> ✅ A behavior trigger

The value is not in the output alone  
but in what it makes you **do next**

***

## 📄 License

MIT

