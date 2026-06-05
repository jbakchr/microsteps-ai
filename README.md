# microsteps-ai

A simple, local AI CLI tool that helps reduce friction when starting tasks by generating small, actionable micro-steps.

---

## 🧠 Purpose

This project is **not** about productivity or planning.  
It is about:

✅ Helping initiate action in the real world  

The goal is not:
- to generate “perfect” steps  
- to optimize completion  

The goal is:

✅ To make starting feel easy  

---

## 🎯 Success Criteria

The system is successful if:

- ✅ You start doing something  
- ✅ The first step feels easy  
- ✅ Resistance is reduced  

---

## ⚙️ How It Works

The system follows a simple loop:

```

input → generate → act

```

- You provide a task (e.g. “clean kitchen”)  
- The system generates **3 small micro-steps**  
- You act immediately (ideally without overthinking)  

---

## ✅ Example Output

```

👉 Step 1: Pick up one plate

Step 2: Put it in the sink
Step 3: Turn on the tap

```

---

## 🧠 Key Learnings So Far

- ✅ **Specific inputs → much better outputs**
  - "clean kitchen" > "clean apartment"

- ✅ **Step 1 is everything**
  - It must feel almost trivial

- ✅ **Momentum matters more than structure**
  - Steps 2–3 are optional

- ✅ **Physical actions work best**
  - Avoid thinking/planning steps

- ✅ The system works even if outputs are imperfect

- ❗ The biggest risk is **not using the tool**

---

## ⚡ Usage (zero setup behavior)

### Run from anywhere:

```bash
microsteps
```

Then:

```
What do you want to do?

> clean kitchen
```

→ Start immediately

***

## 🚀 Installation

### Requirements

* Python 3.11+
* Ollama running locally

***

### Install CLI globally

From project root:

```bash
pip install -e .
```

This makes the CLI available globally:

```bash
microsteps
```

***

## 🧱 Project Structure

```
microsteps/
├── core/           → behavior + generation logic
│
interfaces/
└── cli/           → command-line interface

docs/
└── FEEDBACK.md    → real-world usage logging
```

***

## 🧠 Architecture Principles

* ✅ Core = **behavior + logic**
* ✅ CLI = **simple and frictionless**
* ✅ System = **local, fast, always available**

There is **no backend server**.

The system is designed to:

> ✅ minimize friction between intention and action

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

✅ **Usage + learning phase**

Focus is on:

* what actually triggers action
* what reduces friction
* what leads to real-world behavior

***

## 🔮 Possible Future Directions

(Only if supported by real usage)

* Input refinement (handling vague tasks)
* Improving Step 1 quality
* Lightweight interaction (minimal)
* Optional UI (only if it improves access)

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

✅ **a behavior trigger**

The value is not in the output itself  
but in:

> what it makes you do next

***

## 📄 License

MIT

