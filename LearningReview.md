# Tony's Python Learning Review

**Days completed: 1–10 | Environment: Python 3.14, IntelliJ**
**Last updated: 2026-05-02**

---

## Day 1 — Hello World

### Lesson
- Install Python 3, set up IntelliJ
- Run first script: `python hello.py`
- Understand the REPL — no Java equivalent
- Key difference: no `public static void main`, no semicolons, no braces

### Exercises
- Print "Hello World"

### What I Did
- Ran first script successfully

---

## Day 2 — Variables & Types

### Lesson
- Dynamic typing vs Java's static typing
- Primitives: `int`, `float`, `str`, `bool`
- `type()` function — like `instanceof` but for inspection
- Multiple assignment: `x, y, z = 1, 2, 3`
- Chained assignment: `a = b = 12`
- f-strings vs Java's `String.format()` — including format specifiers like `{price:.2f}`

### Exercises
- Declare variables of each type and inspect with `type()`
- Build an f-string with multiple values and formatting

### What I Did
- Used multiple assignment and chained assignment correctly
- Applied f-string formatting with `:.2f` for floats

---

## Day 3 — Control Flow

### Lesson
- `if / elif / else` — no `switch` until Python 3.10's `match`
- `for` loops: `for item in collection` — like Java's enhanced for-each
- `while` loops — identical concept to Java
- No `do-while` in Python
- `range(start, stop, step)` for numeric loops
- `enumerate()` for index + value iteration
- `match` statement (Python 3.10+) — Python's switch

### Exercises
- Grade calculator using `if/elif/else`
- Loop over a list with `enumerate()`
- `while` loop with a flag

### What I Did
- Implemented grade calculator correctly
- Explored `match` with guard conditions (`case val if val >= 90`) — beyond lesson scope
- Used `range()` with step

---

## Day 4 — Functions

### Lesson
- `def` keyword vs Java's method signatures
- No return type declaration, no access modifiers
- Default arguments: `def greet(name, greeting="Hello")`
- Keyword arguments: caller names the parameter explicitly, order doesn't matter
- `*args` — variable positional args, stored as a tuple (like Java varargs)
- `**kwargs` — variable keyword args, stored as a dict (no Java equivalent)
- Argument order rule: `positional → default → *args → **kwargs`

### Exercises
- `power(base, exp=2)` — returns base raised to exp
- `summarize(*items)` — prints each item numbered
- `build_query(**filters)` — prints SQL-style `WHERE key = value` for each filter

### What I Did
- Extended `build_query` to accept a `table` positional arg and build real SQL with `WHERE`/`AND` — strong backend instinct
- Used keyword args correctly in calls (`base=4, exp=4`)

---

## Day 5 — Collections

### Lesson
- `list` → like `ArrayList<T>` — slicing, `append`, `remove`, `pop`, stack and queue patterns
- `tuple` → immutable list — unpacking, `enumerate()`
- `dict` → like `HashMap<K,V>` — CRUD, `get()` with default, `items()` iteration, `del`, `pop()`
- `set` → like `HashSet<T>` — `add`, `discard`, `in`, set ops (`&`, `|`, `-`)
- List comprehensions: `[expr for x in iterable if condition]`
- `deque` from `collections` for efficient queues
- Negative indexing: `[-1]` last, `[-2:]` last two
- Slicing: `[start:stop:step]` — start inclusive, end exclusive

### Exercises
- List of 5 numbers — find max, min, sum without a loop
- Dict representing a product — safely get a missing key with default
- Set of tags — add, remove, check membership
- List comprehension filtering even numbers and squaring them from 1–10

### What I Did
- Used list as stack and queue (with `deque`) correctly
- Tuple unpacking and `enumerate()` on a tuple
- Created a function called inside a list comprehension
- Fixed variable naming (`list` → `list_of_nums`) after feedback
- Used `range(1, 11)` pattern after correction

---

## Day 6 — Strings

### Lesson
- Strings are immutable — same as Java
- Slicing: `s[start:stop:step]` — works just like list slicing
- `s[::-1]` — reverse a string using step of -1
- Common methods: `.strip()`, `.lstrip()`, `.rstrip()`, `.upper()`, `.lower()`, `.capitalize()`, `.title()`
- `.replace()`, `.split()`, `.join()`, `.find()`, `.count()`, `.startswith()`, `.endswith()`
- `in` operator for membership — like Java's `.contains()`
- Multi-line strings with triple quotes — useful for SQL, HTML
- String formatting: f-strings (preferred), `.format()` (older), `%` (avoid)

### Exercises
- Strip, lowercase, title-case `"  python is GREAT  "`
- Split `"apple,banana,orange"` and rejoin with `" | "`
- Check if `"world"` is in `"hello world"` and find its index
- Multi-line f-string user profile
- Reverse `"backend"` using slicing

### What I Did
- Used `assert` throughout instead of `print` — already thinking in tests
- Created `utils/helper.py` module independently
- Discovered and used the **walrus operator** (`:=`) unprompted in Exercise 3

**Parking Lot answered:**
- `s[::-1]` — slice step notation; `[::-1]` traverses string backwards. Full form: `[start:stop:step]`

---

## Day 7 — Practice + pytest

### Lesson
- Classic practice problems: FizzBuzz, reverse a string, word frequency counter
- pytest basics — test discovery, no boilerplate needed
- File naming: `test_*.py`, function naming: `test_*()`
- `assert` replaces JUnit's `assertEquals`, `assertTrue`
- Run with `pytest` or `pytest -v` for verbose output
- Import implementation from separate file: `from day07_practice import *`
- Virtual environments: `.venv` isolates dependencies per project
- `requirements.txt` — lists dependencies; IntelliJ auto-detects and installs
- `pip install -r requirements.txt` — equivalent of `mvn install`

### Exercises
- Implement `fizzbuzz(n)` — returns FizzBuzz values from 1 to n
- Implement `reverse_str(s)` — reverses a string
- Implement `word_freq_counter(text)` — returns dict of word counts
- Write at least 2 pytest tests per function in `test_day07.py`

### What I Did
- Wrote 6 tests covering normal and edge cases (zero input, None input)
- Stripped punctuation using `isalnum()` and `isspace()` — went beyond spec
- Fixed `word_freq_counter` bug (used `setdefault` incorrectly) → replaced with `dict.get(word, 0) + 1`
- Removed side effects (`helper.lesson()`) from inside functions after feedback

**Parking Lot answered:**
- `==` on lists vs sets — list `==` is order-sensitive; set `==` is value-only (like `ArrayList` vs `HashSet`)
- `str.maketrans` and `.translate()` — `maketrans()` builds a char mapping table; `.translate()` applies it — bulk char replacement/deletion
- Virtual environments & `requirements.txt` — `.venv` isolates deps per project; IntelliJ auto-detects both

---

## Day 8 — Pythonic Idioms & Java Developer Gotchas

### Lesson
- Variable swapping: `a, b = b, a`
- Chained comparisons: `0 < x < 10`
- Ternary expressions: `x if condition else y` — chain with parens for multi-line
- Splat unpacking: `first, *middle, last = lst` — `*` always captures a list
- `_` as throwaway variable in unpacking and loops
- Truthiness: falsy values are `None`, `0`, `""`, `[]`, `{}`, `()`
- Mutable default arguments — use `None` sentinel, never `[]` or `{}`
- `==` vs `is` — always use `is None`, never `== None`
- Integer division: `/` returns float; `//` for floor division; `-7 // 2 == -4` (floors, not truncates)
- `None` is a singleton object, not just "no reference" — `is None` is identity check
- No `++` — use `+=`
- Indentation is syntax
- Shadowing built-ins silently breaks things

### Exercises
- `swap(a, b)` — one-line body
- `is_valid_port(n)` — chained comparison
- `classify(n)` — chained ternary with parens
- Splat unpacking variations: middle, first, last
- `merge_collections`, `merge_dictionaries` with splat
- `name_year_only(t)` — `_` discard
- `summarize(items)` — truthiness
- `add_tag` (buggy) and `add_tag_safe` (fixed with `is None`)
- `identity_gotchas()` — `==` vs `is` demo
- `divide(a, b)` — float and floor results
- `safe_double(n)` — `is None` guard

### What I Did
- Used parens for multi-line ternary unprompted — clean
- Explored all three splat positions (first, middle, last) plus merge variants
- Strong boundary testing on `is_valid_port` (0, 1, 65535, 65536)
- Initially used `if not tags` in `add_tag_safe` — caught and fixed to `if tags is None`
- Initially implemented `safe_double` as squaring (`n ** 2`) — caught and fixed to `n * 2`
- Removed `common_none_falsy_trap` from tests after incorrect comment rather than fixing — acceptable

### Parking Lot answered
- None — no items resolved this session (enums and dunders deferred to Day 13)

---

## Day 9 — List Comprehensions & Generators

### Lesson
- List comprehensions: filter + transform in one expression — like Java streams but more concise
- Dict and set comprehensions: `{k: v for ...}`, `{x for ...}`
- Nested comprehensions: outer loop first, inner loop second
- Generator expressions: lazy evaluation, one-shot iteration — like Java `Stream<T>`
- `yield` keyword: turns a function into an iterator, pauses and resumes execution
- `zip()`: parallel iteration over two sequences
- `map(fn, iterable)`: apply function to every element — prefer comprehension for readability, `map` for named functions
- `filter(fn, iterable)`: keep elements where fn returns True
- `sorted()` with `key`: extract sort value via function — like `Comparator.comparing()`
- Multi-key sort: return a tuple from `key`; negate numeric fields for descending order
- `sorted()` vs `.sort()`: sorted returns new list, sort is in-place

### Exercises
- `squares_of_evens(nums)` — list comprehension with filter
- `flatten(matrix)` — nested comprehension
- `word_lengths(words)` — dict comprehension
- `first_n_squares(n)` — generator with `yield`
- `big_sum(limit)` — generator expression passed to `sum()`
- `pair_up(keys, values)` — `zip()` into dict
- `apply_all(fn, items)` — `map()`
- `keep_if(predicate, items)` — `filter()`
- `sort_by_length(words)` — `sorted()` with built-in key
- `sort_people(people)` — multi-key sort with negation for descending

### What I Did
- Applied `None` guards consistently across all functions using `is None`
- Used `if word` in `word_lengths` to filter `None` and empty strings in one shot
- Used `-p[1]` negation correctly for descending age sort
- Wrote thorough tests including edge cases (empty list, None input, mixed None elements)
- Tests written to match spec (age descending), not just implementation

### Parking Lot answered
- Java Comparators → `sorted()` with `key` function covered this session

---

## Day 10 — File I/O

### Lesson
- `open()` with `with` statement — auto-closes file, like Java try-with-resources
- Modes: `"r"`, `"w"`, `"a"`, `"x"`, `"r+"`, `"w+"`, `"a+"` — multi-mode needs `seek(0)` to rewind
- `f.read()`, `f.readline()`, `f.readlines()`, `for line in f` — four grains of reading
- `f.write()` vs `f.writelines()` — neither adds newlines automatically
- `csv.DictReader` / `csv.DictWriter` — dict-based CSV I/O; headers inferred from first dict's keys
- CSV always returns strings — cast manually or use pandas for typed reading
- `pathlib.Path` — modern path handling; `/` operator joins paths; `Path()` is idempotent
- `path.parent.mkdir(parents=True, exist_ok=True)` — create missing dirs before writing

### Exercises
- `write_lines(filepath, lines)` / `read_lines(filepath)` — text file round-trip
- `write_csv(filepath, rows)` / `read_csv(filepath)` — CSV round-trip with dicts
- Updated both write functions to accept `str` or `Path` and auto-create parent dirs

### What I Did
- Used `tmp.` prefix naming for temp files — already gitignored by project convention
- Switched `read_csv` to `list(csv.DictReader(f))` after feedback — cleaner
- Applied `Path(filepath)` directly in `write_csv` (idempotent); kept `isinstance` check in `write_lines` — inconsistency between the two similar functions
- Good instinct on pass-by-value vs rebinding — correctly identified that `lst = [99]` inside a function doesn't mutate the caller's list

### Parking Lot answered
- None — all open items deferred to future lessons

---

## Pythonic Idioms Picked Up Along the Way

| Idiom | Notes |
|---|---|
| Tuple unpacking | `x, y = point` |
| `enumerate()` on any iterable | replaces manual index tracking |
| Negative indexing | `[-1]` last, `[-2:]` last two |
| Slicing | `[start:stop:step]` — start inclusive, end exclusive, same as Java's `subList` |
| `in` for membership checks | replaces `.contains()` — works on lists, sets, dicts, strings |
| `deque` for efficient queues | `list.pop(0)` is O(n); `deque.popleft()` is O(1) |
| `Decimal("0.1")` for precision | like `BigDecimal` — always pass as string |
| Nested quotes in f-strings | works in Python 3.12+; breaks on older runtimes |
| Walrus operator (`:=`) | assign + evaluate in one expression: `if (i := s.find("x")) > -1` |
| `dict.get(key, 0) + 1` | Pythonic counting pattern — avoids `KeyError` |
| `a, b = b, a` | swap without temp variable |
| Chained comparisons | `0 < x < 10` — reads like math, short-circuits |
| Ternary with parens | `("x" if a else "y" if b else "z")` — multi-line ternary chain |
| Splat unpacking `*` | `first, *middle, last = lst` — `*` always gives a list |
| `_` throwaway | convention for intentionally ignored values |
| `if tags is None: tags = []` | safe mutable default pattern |
| `x is None` / `x is not None` | always use `is` for None checks, never `==` |
| Generator expression in function call | `sum(x**2 for x in data)` — no extra `[]` needed |
| Negate numeric key for descending sort | `key=lambda p: (-p[1], p[0])` — age desc, name asc |
| `map(len, words)` | pass built-in directly to map — no lambda needed |
| `Path(filepath)` is idempotent | wraps `str` or `Path` — always safe, no `isinstance` check needed |
| `path.parent.mkdir(parents=True, exist_ok=True)` | create missing dirs before writing — like `mkdir -p` |
| `list(csv.DictReader(f))` | cleaner than list comprehension for materializing a reader |
| `newline=""` on CSV write | prevents blank lines on Windows — include by habit even on Mac |

---

## Observations & Habits to Watch

**Strengths:**
- Extends exercises beyond requirements — SQL builder, composer filter, `match` guards, punctuation stripping, splat variations
- Good data structure instincts from Java (choosing `deque`, thinking about edge cases)
- Clean use of `enumerate()` and unpacking throughout
- Already thinking in tests — uses `assert` over `print`, writes edge cases unprompted
- Fixes bugs quickly and cleanly when pointed out
- Self-directed — created `utils/helper.py` module independently
- Strong boundary testing instinct (port numbers: 0, 1, 65535, 65536)
- Asks sharp conceptual questions (None vs null, `is` vs `==`, REPL vs script context)

**Watch out for:**
- Using built-in names as variables (`list`, `dict`) — shadows Python built-ins
- `range(0, 10)` with `i+1` inside — prefer `range(1, 11)` for clarity
- PEP 8 spacing: no space before `:`, spaces inside tuple destructuring `(k, v)`
- Side effects inside functions (e.g. `helper.lesson()` inside `fizzbuzz()`)
- `if x in dict.keys()` → prefer `if x in dict`
- Truthiness checks (`if not x`) when `None` is the specific target — use `is None`

---

*This file is updated as lessons are completed. See Syllabus.md for full progress tracking.*
