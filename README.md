# microsteps-ai

A simple local AI service that turns tasks into small, actionable micro-steps.

## Goal

Help reduce friction when starting tasks by generating extremely small, easy-to-begin steps.

## Example

Input:

    Clean my apartment

Output:

    - Pick up visible trash in one room
    - Put dishes in the sink
    - Clear one small surface
    - Set a 10-minute timer and clean
    - Take a short break

## Requirements

- Python 3.11+
- Ollama running locally

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

## Test

```bash
curl -X POST http://localhost:8000/generate-microsteps \
  -H "Content-Type: application/json" \
  -d '{"task": "Start writing my CV"}'
```

## Notes (as of now)

- No persistence (by design)
- No frontend (yet)
- Focus is purely on micro-step generation

## Future Ideas

- CLI wrapper
- Desktop quick-capture tool
- Task categories
- Energy-aware prompts

## License

MIT
