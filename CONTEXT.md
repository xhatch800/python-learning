# Session Context

> Handoff notes for new chat sessions — things not captured in CLAUDE.md, Syllabus.md, or LearningReview.md.
> Updated after each lesson completion.

---

## Environment
- Python 3.14 (IntelliJ) — do NOT flag nested quotes in f-strings as errors, this is valid in 3.12+
- Sandbox runs Python 3.10 — always run files with `PYTHONPATH=. python3` from project root
- pytest 9.0.3 installed in `.venv`
- `requirements.txt` at project root

## Project Structure Notes
- `week01/` through `week04/` — lesson code files live here
- `adhoc/` — free-play sandbox, ignore when checking work
- `utils/helper.py` — custom helper module Tony built; lesson files import it with `from utils import helper`
- `CLAUDE_proposed.md` — leftover file, can be deleted

## Tony's Goals & Philosophy
- Evaluating Python seriously as a production/enterprise language, not just learning as a hobby
- Java-fluent backend developer — frame everything through Spring Boot / Java equivalents
- Genuinely interested in production concerns: caching, rate limiting, Docker, message queues, GIL limitations

## Key Conventions Established
- "next item" — move to next concept in lesson
- "Parking Lot" — log topic to ParkingLot.md and continue without digressing
- "Back on Track" — re-summarize current lesson state
- Lessons are item-by-item with one exercise per item, not batched
- Check work only in relevant week folder, never adhoc/

## Recent Discussions (not yet in lesson files)
- GIL limitations and Python vs Java for high-scalability apps — deferred to Day 20–21
- Dunder methods (`__eq__`, `__hash__`, `__str__`) — deferred to Day 13
- Python for enterprise: viable for APIs, data, ML; GIL limits CPU-bound concurrency
