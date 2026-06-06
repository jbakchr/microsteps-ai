# microsteps-ai

A simple, local AI CLI tool that helps reduce friction when starting tasks.

It does one thing:

> ✅ It makes starting feel easier

---

## 🧠 Why this exists

Starting tasks is often the hardest part.

Not because we don’t know what to do  
—but because the **friction to begin is too high**.

This tool is built on a simple idea:

> ✅ You don’t need better plans  
> ✅ You need easier first steps

---

## 🎯 What it does

You give it a task:

```

clean kitchen

```

It gives you:

```

👉 Step 1: Pick up one plate

Step 2: Put it in the sink
Step 3: Turn on the tap

```

That’s it.

No planning.  
No structure.  
Just something easy enough to start.

---

## ✅ Success criteria

The tool is successful if:

- ✅ You start doing something
- ✅ Step 1 feels almost trivial
- ✅ Resistance is lower than before

---

## ⚙️ Usage

Run from anywhere:

```bash
microsteps
```

Then:

```
What do you want to do?

> clean kitchen
```

→ Start immediately

---

## 🚀 Installation

### Requirements

- Python 3.11+
- Ollama running locally

---

### Install CLI globally

From the project root:

```bash
pip install -e .
```

This makes the command available globally:

```bash
microsteps
```

---

## 🧱 Project structure

```
microsteps/
├── cli.py        → command-line interface
└── generate.py   → micro-step generation logic

docs/
└── FEEDBACK.md   → real-world usage logging
```

---

## 🧠 Core principles

- ✅ Reduce friction to start
- ✅ Prioritize action over planning
- ✅ Keep everything simple and fast
- ✅ Optimize for real-world use, not perfect output

---

## 🧪 Feedback loop

Real usage is tracked in:

```
docs/FEEDBACK.md
```

Each entry captures:

- Input
- Output
- Whether you acted
- How it felt

---

## 🧭 Current focus

This project is in a:

> ✅ usage + learning phase

Focus:

- What actually triggers action
- What makes Step 1 easier
- What reduces friction in practice

---

## 🚫 Non-goals

- Not a productivity system
- Not a task manager
- Not a feature-rich app
- Not optimized for scale

---

## 🧠 Core idea

This is not a tool for generating steps.

It is:

> ✅ a behavior trigger

The value is not in the output itself  
but in:

> what it makes you do next

---

## 📄 License

MIT
