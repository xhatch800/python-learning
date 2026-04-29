# Python Fluency Syllabus (Java Developer Fast-Track)

> **Goal:** Reach Python fluency in ~4 weeks of focused practice (~1–2 hours/day).
> Your Java background cuts the learning curve significantly — most concepts map directly.
> **Track: Web Backend** — building REST APIs with FastAPI + SQLAlchemy (equivalent to Spring Boot in Java).
> **Environment:** Python 3.14 (IntelliJ). Note: some syntax (e.g. nested quotes in f-strings) requires 3.12+ and may not work on older runtimes like servers running ≤ 3.11.

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

### [x] Day 3 — Control Flow
- [x] `if / elif / else` (no `switch` until Python 3.10's `match`)
- [x] `for` loops: `for item in collection` — closer to Java's enhanced for-each
- [x] `while` loops — identical concept
- [x] No `do-while` in Python

### [x] Day 4 — Functions
- [x] `def` keyword vs. Java's method signatures
- [x] No return type declaration, no access modifiers
- [x] Default arguments and keyword arguments (no Java equivalent — very powerful)
- [x] `*args` and `**kwargs` (like varargs, but more flexible)

### [x] Day 5 — Collections
- [x] `list` → like `ArrayList<T>`
- [x] `tuple` → like an immutable list (no direct Java equivalent)
- [x] `dict` → like `HashMap<K, V>`
- [x] `set` → like `HashSet<T>`
- [x] List comprehensions — Java has streams; Python's comprehensions are more concise

### [ ] Day 6 — Strings
- [ ] Strings are immutable (same as Java)
- [ ] Slicing: `s[1:4]` — no Java equivalent, very Pythonic
- [ ] Common methods: `.split()`, `.strip()`, `.join()`, `.replace()`
- [ ] Multi-line strings with triple quotes

### [ ] Day 7 — Practice + Intro to pytest
- [ ] Write FizzBuzz, reverse a string, word frequency counter
- [ ] Rewrite a simple Java backend utility you know in Python (e.g. a data transformer or validator)
- [ ] Install pytest: `pip install pytest`
- [ ] Write your first test file: `test_day07.py` — like a JUnit test class
- [ ] `def test_something():` — no annotations needed, just the `test_` prefix
- [ ] `assert` keyword — like JUnit's `assertEquals`, `assertTrue`
- [ ] Run tests: `pytest` — discovers and runs all `test_*.py` files automatically
- [ ] Test a pure function end-to-end: input → expected output

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

### [ ] Day 14 — Practice + Mocking Basics
- [ ] Build a small CLI app that models a REST-like resource: e.g. a to-do manager with add/list/delete commands
- [ ] Focus on writing idiomatic Python, not Java-translated Python
- [ ] Write tests for your CLI app with `pytest`
- [ ] `unittest.mock.MagicMock` — mock any object or dependency, like `Mockito.mock()`
- [ ] `@patch("module.function")` — replace a real function with a mock for a test, like `@MockBean`
- [ ] Assert mock was called: `mock.assert_called_once_with(arg)` — like `Mockito.verify()`
- [ ] Mock a file read or external call your CLI makes

---

## Week 3 — Standard Library & Ecosystem

### [ ] Day 15–16 — Key Standard Library Modules
- [ ] `os`, `sys` — system/env interaction
- [ ] `json` — like Jackson, but built-in
- [ ] `datetime` — date/time handling
- [ ] `re` — regular expressions
- [ ] `collections` — `Counter`, `defaultdict`, `deque`
- [ ] `itertools` — advanced iteration utilities

### [ ] Day 17–18 — Data & Scripting + Intermediate Mocking
- [ ] `csv` and `json` file processing
- [ ] `argparse` — CLI argument parsing
- [ ] `logging` — like Java's SLF4J/Logback
- [ ] `pytest-mock` — cleaner `mocker` fixture: `mocker.patch()` vs `@patch` decorator
- [ ] Mock a service class — patch a method on an object, like mocking a `@Service` in Spring
- [ ] `side_effect` — simulate exceptions or dynamic return values from mocks
- [ ] `pytest` fixtures — reusable setup/teardown, like JUnit `@BeforeEach`
- [ ] Parametrized tests: `@pytest.mark.parametrize` — run same test with multiple inputs

### [ ] Day 19–20 — Concurrency Basics
- [ ] `threading` vs. `multiprocessing` (understand the GIL)
- [ ] `asyncio` basics — Python's async/await (similar to Java's CompletableFuture)

### [ ] Day 21 — Calling APIs (Authenticated & Unauthenticated)
- [ ] Install `requests`: `pip install requests`
- [ ] Call a public API (e.g. JSONPlaceholder) — basic GET/POST
- [ ] Call a secured API with an **API key** — pass via header (`Authorization: ApiKey xxx`) or query param
- [ ] Call a secured API with a **Bearer token** — `Authorization: Bearer <token>`
- [ ] OAuth2 **client credentials flow** — machine-to-machine, like service accounts in Spring Security
- [ ] Handle 401 / 403 responses gracefully — retry vs. fail fast
- [ ] Store secrets in env vars, never hardcode — use `python-dotenv`

---

## Week 4 — Web Backend Track (FastAPI)

> **Java equivalent:** Spring Boot → FastAPI. Same concepts: routing, request/response models, dependency injection, ORM.

### [ ] Day 22 — FastAPI Intro
- [ ] Install FastAPI + Uvicorn: `pip install fastapi uvicorn`
- [ ] Create your first endpoint: `@app.get("/")` — like `@GetMapping` in Spring
- [ ] Run the dev server: `uvicorn main:app --reload` — like Spring Boot's hot reload
- [ ] Explore auto-generated Swagger UI at `http://localhost:8000/docs` — free, no setup

### [ ] Day 23 — Request & Response Models
- [ ] Define request bodies with `pydantic` — like Java records / DTOs
- [ ] Path params: `@app.get("/users/{id}")` — like `@PathVariable`
- [ ] Query params: `def get_users(active: bool = True)` — like `@RequestParam`
- [ ] Return JSON automatically — no `@ResponseBody` needed

### [ ] Day 24 — SQLAlchemy (ORM)
- [ ] Install: `pip install sqlalchemy`
- [ ] Define models — like JPA `@Entity`
- [ ] Connect to SQLite for local dev, Postgres for prod
- [ ] Basic CRUD: create, read, update, delete — like `JpaRepository`

### [ ] Day 25 — Advanced FastAPI
- [ ] Dependency injection: `Depends()` — like Spring's `@Autowired`
- [ ] Middleware and exception handlers — like `@ControllerAdvice`
- [ ] Background tasks — like `@Async`
- [ ] Environment config with `pydantic-settings` — like Spring's `application.properties`

### [ ] Day 25b — Securing Your FastAPI
- [ ] **API key auth** — validate key via `Depends()`, simplest approach for internal services
- [ ] **JWT auth** — issue and verify tokens with `python-jose`; like Spring Security + JWT filter
- [ ] **OAuth2 password flow** — FastAPI has built-in `OAuth2PasswordBearer`
- [ ] **OAuth2 client credentials** — for service-to-service auth (no user involved)
- [ ] Protect routes with `Depends(get_current_user)` — like `@PreAuthorize` in Spring
- [ ] Scopes and role-based access — like Spring's `hasRole()`
- [ ] HTTPS, CORS config — like Spring's `CorsConfigurationSource`

### [ ] Day 26 — Testing & Mocking
- [ ] `pytest` + FastAPI's `TestClient` — like Spring's `MockMvc`
- [ ] Write unit tests for endpoints
- [ ] Test request validation and error responses
- [ ] `unittest.mock` — built-in mocking library, like Mockito in Java
- [ ] `MagicMock` — mock any object, assert calls: like `Mockito.mock()` + `verify()`
- [ ] `@patch` decorator — swap out a dependency for a test: like `@MockBean` in Spring
- [ ] `pytest-mock` — cleaner `mocker` fixture for pytest: `mocker.patch("module.ClassName")`
- [ ] Mock DB calls — patch SQLAlchemy session so tests don't hit a real DB
- [ ] Mock external API calls — patch `requests.get` to return a fake response
- [ ] Mock auth dependencies — override `Depends(get_current_user)` in `TestClient`

### [ ] Day 27 — Project
- [ ] Build a small REST API: a user/post API with full CRUD + JWT-protected routes
- [ ] Add a service that calls an external secured API using Bearer token
- [ ] Use FastAPI + SQLAlchemy + pytest
- [ ] Structure it as a proper package (routers, models, schemas, db, auth)

### [ ] Day 28 — Review & Gaps
- [ ] Go back and reinforce anything that felt weak
- [ ] Read: *PEP 8* (Python style guide), *The Zen of Python* (`import this`)
- [ ] Next steps: refresh token rotation, rate limiting, API gateway patterns

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
- [FastAPI Docs](https://fastapi.tiangolo.com) — excellent, thorough, beginner-friendly
- [SQLAlchemy Docs](https://docs.sqlalchemy.org) — the ORM you'll use daily
- [Real Python](https://realpython.com) — practical tutorials
- [Exercism Python Track](https://exercism.org/tracks/python) — structured exercises
- [Fluent Python (book)](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) — deep dive for serious fluency
