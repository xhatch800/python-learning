# Python Fluency Syllabus (Java Developer Fast-Track)

> **Goal:** Reach Python fluency in ~4 weeks of focused practice (~1–2 hours/day).
> Your Java background cuts the learning curve significantly — most concepts map directly.

**Progress:** Check off each item as you complete it. Use the day checkboxes to mark full days done.

---

## Week 1 — Python Basics (Java Translation Layer)

The goal this week is to rewire Java muscle memory into Python syntax.

### [x] Day 1 — Setup & Hello World
- [x] Install Python 3, set up VS Code or PyCharm
- [x] Run your first script: `python hello.py`
- [x] Understand the REPL (`python` interactive shell) — no Java equivalent, but invaluable
- [x] **Key difference:** No `public static void main`, no semicolons, no braces

### [x] Day 2 — Variables & Types
- [x] Dynamic typing vs. Java's static typing
- [x] Primitives: `int`, `float`, `str`, `bool`
- [x] `type()` function — like `instanceof` but for inspection
- [x] f-strings vs. Java's `String.format()`

### [ ] Day 3 — Control Flow
- [ ] `if / elif / else` (no `switch` until Python 3.10's `match`)
- [ ] `for` loops: `for item in collection` — closer to Java's enhanced for-each
- [ ] `while` loops — identical concept
- [ ] No `do-while` in Python

### [ ] Day 4 — Functions
- [ ] `def` keyword vs. Java's method signatures
- [ ] No return type declaration, no access modifiers
- [ ] Default arguments and keyword arguments (no Java equivalent — very powerful)
- [ ] `*args` and `**kwargs` (like varargs, but more flexible)

### [ ] Day 5 — Collections
- [ ] `list` → like `ArrayList<T>`
- [ ] `tuple` → like an immutable list (no direct Java equivalent)
- [ ] `dict` → like `HashMap<K, V>`
- [ ] `set` → like `HashSet<T>`
- [ ] List comprehensions — Java has streams; Python's comprehensions are more concise

### [ ] Day 6 — Strings
- [ ] Strings are immutable (same as Java)
- [ ] Slicing: `s[1:4]` — no Java equivalent, very Pythonic
- [ ] Common methods: `.split()`, `.strip()`, `.join()`, `.replace()`
- [ ] Multi-line strings with triple quotes

### [ ] Day 7 — Practice
- [ ] Write 3–5 small programs: FizzBuzz, reverse a string, word frequency counter
- [ ] Rewrite a simple Java program you know in Python

---

## Week 2 — Pythonic Thinking

The goal this week is to stop writing "Java in Python" and start writing real Python.

### [ ] Day 8 — List Comprehensions & Generators
- [ ] `[x*2 for x in nums if x > 0]` vs. Java streams
- [ ] Generator expressions for memory-efficient iteration
- [ ] `zip()`, `enumerate()`, `map()`, `filter()`

### [ ] Day 9 — File I/O
- [ ] `open()`, `with` statement (like Java's try-with-resources)
- [ ] Reading/writing text files and CSVs
- [ ] `pathlib` — modern file path handling

### [ ] Day 10 — Error Handling
- [ ] `try / except / finally / else` — similar to Java's `try/catch/finally`
- [ ] Raising exceptions: `raise ValueError("msg")`
- [ ] Custom exception classes

### [ ] Day 11 — Modules & Packages
- [ ] `import`, `from x import y`
- [ ] Organizing code into `.py` files and folders
- [ ] `pip` — Python's equivalent of Maven/Gradle
- [ ] Virtual environments: `venv`

### [ ] Day 12 — OOP in Python
- [ ] `class`, `__init__` (constructor), `self` (like `this`)
- [ ] Inheritance, method overriding
- [ ] `@property` decorator vs. Java getters/setters
- [ ] No interfaces — use abstract classes (`abc`) or duck typing

### [ ] Day 13 — Functional Python
- [ ] First-class functions (pass functions as arguments)
- [ ] `lambda` — like Java lambdas but simpler
- [ ] `functools`: `reduce`, `partial`
- [ ] Decorators — like Java annotations but executable

### [ ] Day 14 — Practice
- [ ] Build a small CLI app: a to-do list, a text-based quiz, or a file organizer
- [ ] Focus on writing idiomatic Python, not Java-translated Python

---

## Week 3 — Standard Library & Ecosystem

### [ ] Day 15–16 — Key Standard Library Modules
- [ ] `os`, `sys` — system/env interaction
- [ ] `json` — like Jackson, but built-in
- [ ] `datetime` — date/time handling
- [ ] `re` — regular expressions
- [ ] `collections` — `Counter`, `defaultdict`, `deque`
- [ ] `itertools` — advanced iteration utilities

### [ ] Day 17–18 — Data & Scripting
- [ ] `csv` and `json` file processing
- [ ] `argparse` — CLI argument parsing
- [ ] `logging` — like Java's SLF4J/Logback
- [ ] `unittest` — like JUnit; also learn `pytest`

### [ ] Day 19–20 — Concurrency Basics
- [ ] `threading` vs. `multiprocessing` (understand the GIL)
- [ ] `asyncio` basics — Python's async/await (similar to Java's CompletableFuture)

### [ ] Day 21 — Practice
- [ ] Build a project: a web scraper, a data parser, or a REST API client using `requests`

---

## Week 4 — Real-World Python

### [ ] Day 22–23 — Choose a Domain Track

Pick one based on your goals:

| Track | Libraries to Learn |
|---|---|
| **Data / ML** | `numpy`, `pandas`, `matplotlib`, `scikit-learn` |
| **Web Backend** | `FastAPI` or `Flask`, `SQLAlchemy` |
| **Automation / DevOps** | `subprocess`, `paramiko`, `boto3` (AWS) |
| **Testing / Tooling** | `pytest`, `hypothesis`, `click` |

### [ ] Day 24–25 — Advanced Python
- [ ] Type hints (`x: int`, return types) — like Java types, but optional
- [ ] Dataclasses (`@dataclass`) — like Java records
- [ ] Context managers (`__enter__`, `__exit__`)
- [ ] Slots and memory optimization

### [ ] Day 26–27 — Project
- [ ] Build a complete, working project in your chosen domain
- [ ] Write tests for it
- [ ] Structure it as a proper package

### [ ] Day 28 — Review & Gaps
- [ ] Go back and reinforce anything that felt weak
- [ ] Read: *PEP 8* (Python style guide), *The Zen of Python* (`import this`)

---

## Key Mindset Shifts: Java → Python

| Concept | Java | Python |
|---|---|---|
| Types | Explicit, static | Inferred, dynamic |
| Boilerplate | High (`public static void main`) | Minimal |
| Getters/Setters | Manual or Lombok | `@property` decorator |
| Null | `null` + NullPointerException | `None` + explicit checks |
| Iteration | Iterators, streams | `for x in y`, comprehensions |
| Interfaces | `interface` keyword | Duck typing / `Protocol` |
| Packaging | Maven/Gradle | `pip` + `venv` |
| Main entry | Class with `main` method | `if __name__ == "__main__":` |

---

## Resources

- [Official Python Docs](https://docs.python.org/3/) — the best reference
- [Real Python](https://realpython.com) — practical tutorials
- [Python Koans](https://github.com/gregmalcolm/python_koans) — learn by fixing failing tests
- [Exercism Python Track](https://exercism.org/tracks/python) — structured exercises
- [Fluent Python (book)](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) — deep dive for serious fluency
