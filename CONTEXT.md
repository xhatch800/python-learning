# Session Context

> Handoff notes for new chat sessions — unique context not captured in other project files.
> Updated after each lesson completion.

---

## Environment
- Python 3.14 (IntelliJ) — nested quotes in f-strings are valid, do NOT flag as errors
- Sandbox runs Python 3.10 — always run files with `PYTHONPATH=. python3` from project root
- pytest 9.0.3 installed in `.venv`, `requirements.txt` at project root
- In sandbox, pytest must be run via `PYTHONPATH=. python3 -m pytest` (not on PATH — path changes each session)

## Project Structure Notes
- `utils/helper.py` — custom helper module; some lesson files import it with `from utils import helper`
- `CLAUDE_proposed.md` — leftover file, safe to delete
- Temp files in tests use `tmp.` prefix (e.g. `tmp.test_day10.file.txt`) — covered by `.gitignore`

## Tony's Mindset
- Evaluating Python as a serious production/enterprise language, not just a learning exercise
- Production concerns are a priority — caching, rate limiting, Docker, queues, GIL all matter to him
- Python for enterprise verdict so far: viable for APIs, data, ML; GIL is the key limitation for CPU-bound concurrency
