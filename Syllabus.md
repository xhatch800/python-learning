# Python Fluency Syllabus (Java Developer Fast-Track)

> **Goal:** Reach Python fluency in ~5 weeks of focused practice (~1–2 hours/day).
> Your Java background cuts the learning curve significantly — most concepts map directly.
> **Track: Web Backend** — building REST APIs with FastAPI + SQLAlchemy (equivalent to Spring Boot in Java).
> **Environment:** Python 3.14 (IntelliJ). Note: some syntax (e.g. nested quotes in f-strings) requires 3.12+ and may not work on older runtimes like servers running ≤ 3.11.

**Progress:** Check off each item as you complete it. Use the day checkboxes to mark full days done.

---

## Week 1 — Python Basics (Days 1–7)

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

### [x] Day 6 — Strings
- [x] Strings are immutable (same as Java)
- [x] Slicing: `s[1:4]` — no Java equivalent, very Pythonic
- [x] Common methods: `.split()`, `.strip()`, `.join()`, `.replace()`
- [x] Multi-line strings with triple quotes

### [x] Day 7 — Practice + Intro to pytest
- [x] Write FizzBuzz, reverse a string, word frequency counter
- [x] Rewrite a simple Java backend utility you know in Python (e.g. a data transformer or validator)
- [x] Install pytest: `pip install pytest`
- [x] Write your first test file: `test_day07.py` — like a JUnit test class
- [x] `def test_something():` — no annotations needed, just the `test_` prefix
- [x] `assert` keyword — like JUnit's `assertEquals`, `assertTrue`
- [x] Run tests: `pytest` — discovers and runs all `test_*.py` files automatically
- [x] Test a pure function end-to-end: input → expected output

---

## Week 2 — Pythonic Thinking (Days 8–14)

The goal this week is to stop writing "Java in Python" and start writing real Python.

### [x] Day 8 — Pythonic Idioms & Java Developer Gotchas
> **Living reference** — new idioms and gotchas discovered after Day 8 is completed are appended here. No need to recheck this day.

#### Pythonic Idioms
- [x] Variable swapping without temp: `a, b = b, a`
- [x] Chained comparisons: `0 < x < 10`
- [x] Ternary expressions: `x if condition else y`
- [x] Splat unpacking: `first, *rest = list`
- [x] `_` as throwaway variable
- [x] Truthiness: `if items`, `if not items`, `if user`
- [x] Walrus operator `:=` — assign and evaluate in one expression: `if (i := s.find("x")) > -1`

#### Java Developer Gotchas
- [x] Mutable default arguments — `def f(x=[])` is dangerous; the list persists across calls
- [x] `==` vs `is` — `==` compares value (like Java), `is` compares identity (like `==` on object refs)
- [x] Integer division — `5 / 2` is `2.5` (not `2`); use `5 // 2` for floor division like Java
- [x] `None` is not `0` or `false` — always check `if x is None`, not `if x == None`
- [x] No `++` operator — use `x += 1`
- [x] Indentation is syntax — a misplaced space breaks your code, no braces to save you
- [x] Shadowing built-ins — naming variables `list`, `dict`, `input`, `id` silently breaks things

### [x] Day 9 — List Comprehensions & Generators
- [x] `[x*2 for x in nums if x > 0]` vs. Java streams
- [x] Generator expressions for memory-efficient iteration
- [x] `zip()`, `enumerate()`, `map()`, `filter()`
- [x] `sorted()` with `key` function — Python's equivalent of Java Comparators *(from ParkingLot)*

### [x] Day 10 — File I/O
- [x] `open()`, `with` statement (like Java's try-with-resources)
- [x] Reading/writing text files and CSVs
- [x] `pathlib` — modern file path handling

### [x] Day 11 — Error Handling
- [x] `try / except / finally / else` — similar to Java's `try/catch/finally`
- [x] Raising exceptions: `raise ValueError("msg")`
- [x] Custom exception classes

### [ ] Day 12 — Modules & Packages
- [ ] `import`, `from x import y`
- [ ] Organizing code into `.py` files and folders
- [ ] `pip` — Python's equivalent of Maven/Gradle
- [ ] Virtual environments: `venv`
- [ ] `requirements.txt` — declaring and installing dependencies *(from ParkingLot)*
- [ ] IDE auto-detection of `requirements.txt` and `.venv` in IntelliJ/PyCharm *(from ParkingLot)*

### [ ] Day 13 — OOP in Python
- [ ] `class`, `__init__` (constructor), `self` (like `this`)
- [ ] Inheritance, method overriding — how Python differs from Java *(from ParkingLot)*
- [ ] `@property` decorator vs. Java getters/setters
- [ ] No interfaces — use abstract classes (`abc`) or duck typing

### [ ] Day 14 — Functional Python
- [ ] First-class functions (pass functions as arguments)
- [ ] `lambda` — like Java lambdas but simpler
- [ ] `functools`: `reduce`, `partial`
- [ ] Decorators — like Java annotations but executable
- [ ] Function overloading alternatives in Python — no true overloading, use default args or `*args` *(from ParkingLot)*

---

## Week 3 — Standard Library & Ecosystem (Days 15–21)

### [ ] Day 15 — Practice + Mocking Basics
- [ ] Build a small CLI app that models a REST-like resource: e.g. a to-do manager with add/list/delete commands
- [ ] Focus on writing idiomatic Python, not Java-translated Python
- [ ] Write tests for your CLI app with `pytest`
- [ ] `unittest.mock.MagicMock` — mock any object or dependency, like `Mockito.mock()`
- [ ] `@patch("module.function")` — replace a real function with a mock for a test, like `@MockBean`
- [ ] Assert mock was called: `mock.assert_called_once_with(arg)` — like `Mockito.verify()`
- [ ] Mock a file read or external call your CLI makes

### [ ] Day 16–17 — Key Standard Library Modules
- [ ] `os`, `sys` — system/env interaction
- [ ] `json` — like Jackson, but built-in
- [ ] `datetime` — date/time handling
- [ ] `re` — regular expressions
- [ ] `collections` — `Counter`, `defaultdict`, `deque`
- [ ] `itertools` — advanced iteration utilities
- [ ] `heapq` — priority queue implementation *(from ParkingLot)*

### [ ] Day 18–19 — Data & Scripting + Intermediate Mocking
- [ ] `csv` and `json` file processing
- [ ] `argparse` — CLI argument parsing
- [ ] `logging` — like Java's SLF4J/Logback
- [ ] `pytest-mock` — cleaner `mocker` fixture: `mocker.patch()` vs `@patch` decorator
- [ ] Mock a service class — patch a method on an object, like mocking a `@Service` in Spring
- [ ] `side_effect` — simulate exceptions or dynamic return values from mocks
- [ ] `pytest` fixtures — reusable setup/teardown, like JUnit `@BeforeEach`
- [ ] Parametrized tests: `@pytest.mark.parametrize` — run same test with multiple inputs
- [ ] `pytest-cov` — test coverage reporting, like JaCoCo in Java

### [ ] Day 20–21 — Concurrency Basics
- [ ] `threading` vs. `multiprocessing` (understand the GIL)
- [ ] `asyncio` basics — Python's async/await (similar to Java's CompletableFuture)
- [ ] Deep dive on GIL — what it is, why it exists, real-world implications for high-scalability apps, and how Python works around it *(from ParkingLot)*

---

## Week 4 — Web Backend Track: FastAPI Core (Days 22–28)

### [ ] Day 22 — Calling APIs (Authenticated & Unauthenticated)
- [ ] Install `requests`: `pip install requests`
- [ ] Call a public API (e.g. JSONPlaceholder) — basic GET/POST
- [ ] Call a secured API with an **API key** — pass via header (`Authorization: ApiKey xxx`) or query param
- [ ] Call a secured API with a **Bearer token** — `Authorization: Bearer <token>`
- [ ] OAuth2 **client credentials flow** — machine-to-machine, like service accounts in Spring Security
- [ ] Handle 401 / 403 responses gracefully — retry vs. fail fast
- [ ] Store secrets in env vars, never hardcode — use `python-dotenv`

> **Java equivalent:** Spring Boot → FastAPI. Same concepts: routing, request/response models, dependency injection, ORM.

### [ ] Day 23 — FastAPI Intro
- [ ] Install FastAPI + Uvicorn: `pip install fastapi uvicorn`
- [ ] Create your first endpoint: `@app.get("/")` — like `@GetMapping` in Spring
- [ ] Run the dev server: `uvicorn main:app --reload` — like Spring Boot's hot reload
- [ ] Explore auto-generated Swagger UI at `http://localhost:8000/docs` — free, no setup

### [ ] Day 24 — Request & Response Models
- [ ] Define request bodies with `pydantic` — like Java records / DTOs
- [ ] Path params: `@app.get("/users/{id}")` — like `@PathVariable`
- [ ] Query params: `def get_users(active: bool = True)` — like `@RequestParam`
- [ ] Return JSON automatically — no `@ResponseBody` needed

### [ ] Day 25 — SQLAlchemy (ORM)
- [ ] Install: `pip install sqlalchemy`
- [ ] Define models — like JPA `@Entity`
- [ ] Connect to SQLite for local dev, Postgres for prod
- [ ] Basic CRUD: create, read, update, delete — like `JpaRepository`
- [ ] Connection pooling — SQLAlchemy built-in, like HikariCP in Spring

### [ ] Day 26 — Advanced FastAPI
- [ ] Dependency injection: `Depends()` — like Spring's `@Autowired`
- [ ] Middleware and exception handlers — like `@ControllerAdvice`
- [ ] Background tasks — like `@Async`
- [ ] Environment-based config with `pydantic-settings` — dev/staging/prod profiles like Spring
- [ ] Caching — `functools.lru_cache` for in-memory, Redis via `redis-py` for distributed
- [ ] Rate limiting — `slowapi` library, like Spring's `@RateLimiter`
- [ ] Health checks & readiness probes — `/health` endpoint for Kubernetes/cloud deployments
- [ ] Structured logging — JSON logging with `structlog` for Datadog/Splunk aggregation

### [ ] Day 27 — Securing Your FastAPI
- [ ] **API key auth** — validate key via `Depends()`, simplest approach for internal services
- [ ] **JWT auth** — issue and verify tokens with `python-jose`; like Spring Security + JWT filter
- [ ] **OAuth2 password flow** — FastAPI has built-in `OAuth2PasswordBearer`
- [ ] **OAuth2 client credentials** — for service-to-service auth (no user involved)
- [ ] Protect routes with `Depends(get_current_user)` — like `@PreAuthorize` in Spring
- [ ] Scopes and role-based access — like Spring's `hasRole()`
- [ ] HTTPS, CORS config — like Spring's `CorsConfigurationSource`

### [ ] Day 28 — Testing & Mocking
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

---

## Week 5 — Production-Grade Python (Days 29–32)

> Taking FastAPI apps from working to production-ready: containerization, async jobs, and final project.

### [ ] Day 29 — Docker
- [ ] Write a `Dockerfile` for your FastAPI app
- [ ] Build and run the container locally
- [ ] `docker-compose` — run app + Postgres + Redis together locally
- [ ] Environment variables in containers — like Spring's `application.properties` per env
- [ ] Multi-stage builds — keep image size small

### [ ] Day 30 — Message Queues
- [ ] Celery — Python's async task queue, like Spring `@Async` + RabbitMQ
- [ ] Redis as a Celery broker — simple setup for background jobs
- [ ] Define and dispatch tasks: `@app.task` decorator
- [ ] Integrate Celery with FastAPI — offload slow work from request cycle
- [ ] Monitor tasks — Flower dashboard for Celery

### [ ] Day 31 — Project
- [ ] Build a small REST API: a user/post API with full CRUD + JWT-protected routes
- [ ] Add a service that calls an external secured API using Bearer token
- [ ] Add Redis caching, rate limiting, and a health check endpoint
- [ ] Use FastAPI + SQLAlchemy + pytest + Docker
- [ ] Structure it as a proper package (routers, models, schemas, db, auth)

### [ ] Day 32 — Review & Gaps
- [ ] Go back and reinforce anything that felt weak
- [ ] Read: *PEP 8* (Python style guide), *The Zen of Python* (`import this`)
- [ ] Next steps: refresh token rotation, API gateway patterns, observability

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
