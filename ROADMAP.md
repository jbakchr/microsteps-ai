# microsteps-ai – Roadmap

This document captures potential future directions for the project.

The purpose is **not to commit to building these features**,  
but to remember ideas and avoid losing them while staying focused  
on the current experimental phase.

---

## 🧭 Current Focus (Do NOT expand yet)

- Generate micro-steps for starting tasks
- Improve prompt quality
- Learn what works through real usage
- Document experience in `FEEDBACK.md`

---

## 💡 Possible Future Enhancements

### 1. Simple CLI Tool

A small CLI wrapper for daily usage, e.g.:

```

ms "clean kitchen"

```

Purpose:

- faster interaction
- reduce friction when using the tool

---

### 2. Desktop “Quick Capture” Tool

A minimal UI (possibly Electron/Tauri) with:

- single input field
- instant micro-step generation
- always available while working

Purpose:

- make the tool part of daily workflow
- reduce friction at the moment of need

---

### 3. Improved Input Handling

#### a) Guiding the user

Help transform vague inputs:

```

clean apartment → suggest: clean kitchen / living room / bathroom

```

#### b) Automatic narrowing

System internally selects a starting area for broad tasks

---

### 4. Different Modes

Possible modes depending on situation:

- **Start mode** (current focus)
  - ultra-small steps
  - focused on initiation

- **Execution mode**
  - slightly larger, more productive steps

- **Low-energy mode**
  - even lower barrier steps

---

### 5. Better Output Experience

- clearer formatting (CLI or UI)
- visually structured steps
- possibly one-step-at-a-time interaction

---

### 6. Learning From Feedback (later stage)

Use patterns from `FEEDBACK.md` to:

- improve prompts
- adjust step style
- detect what leads to action

Note:
This should only be explored after enough real usage data has been collected.

---

## 🚫 What NOT to do (for now)

To keep focus:

- Do not build persistence/database
- Do not add user accounts
- Do not build complex UI yet
- Do not implement memory/context systems

---

## 🧠 Guiding Principle

The goal is not to build a feature-rich system.

The goal is to learn:

> **What actually helps me start doing things.**

All future development should be based on that.
