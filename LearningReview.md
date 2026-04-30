# Tony's Python Learning Review

**Days completed: 1–7 | Environment: Python 3.14, IntelliJ**
**Last updated: 2026-04-30**

---

## Day 1 — Hello World
- Ran first Python script, understood no `main()`, no semicolons, no braces

## Day 2 — Variables & Types
- Dynamic typing, multiple assignment (`x, y, z = 1, 2, 3`), chained assignment (`a = b = 12`)
- `type()`, f-strings with formatting (`{gas_price:.2f}`)

## Day 3 — Control Flow
- `if/elif/else`, `for` with `enumerate()`, `range()` with step, `while`, `match` (Python 3.10+ switch)
- Explored `match` with guard conditions (`case val if val >= 90`) — beyond the lesson scope

## Day 4 — Functions
- `def`, default args, keyword args, `*args` (tuple), `**kwargs` (dict)
- Built a real SQL query builder with `build_query(table, **filters)` — strong backend instinct

## Day 5 — Collections
- `list`: slicing, stack (`append`/`pop`), queue (`deque`/`popleft`)
- `tuple`: unpacking, `enumerate()`
- `dict`: CRUD, `get()` with default, `items()` iteration, `del`
- `set`: `add`, `discard`, membership (`in`), set operations (`&`, `|`, `-`)
- List comprehensions: filtering, transforming, calling functions inside comprehensions

## Day 6 — Strings
- Slicing with `[start:stop:step]` including reverse with `[::-1]`
- Common methods: `.strip()`, `.split()`, `.join()`, `.replace()`, `.upper()`, `.title()`
- Membership: `in`, `.startswith()`, `.endswith()`, `.find()`, `.count()`
- Multi-line strings with triple quotes — used for SQL-style queries
- String formatting: f-strings (preferred), `.format()`, `%` (avoid)
- Used `assert` throughout instead of `print` — already thinking in tests
- Created `utils/helper.py` module independently — self-directed package organization
- Discovered and used the **walrus operator** (`:=`) unprompted

**Parking Lot answered:**
- `s[::-1]` — slice step notation; `[::-1]` traverses string backwards. Full form: `[start:stop:step]`

## Day 7 — Practice + pytest
- Implemented FizzBuzz, reverse string, word frequency counter
- Wrote 6 pytest tests covering normal and edge cases (zero input, None input)
- Cleaned punctuation from strings using `isalnum()` and `isspace()` — went beyond spec
- Used `dictionary.get(word, 0) + 1` — the Pythonic counting pattern
- Understood pytest discovery, `assert`, and separation of implementation vs test files
- Learned virtual environment setup, `requirements.txt`, and IntelliJ auto-install flow

**Parking Lot answered:**
- `==` on lists vs sets — list `==` is order-sensitive; set `==` is value-only (like `ArrayList` vs `HashSet`)
- `str.maketrans` and `.translate()` — `maketrans()` builds a char mapping table; `.translate()` applies it
- Virtual environments & `requirements.txt` — `.venv` isolates deps per project; IntelliJ auto-detects both

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

---

## Observations & Habits to Watch

**Strengths:**
- Extends exercises beyond requirements — SQL builder, composer filter, `match` guards, punctuation stripping
- Good data structure instincts from Java (choosing `deque`, thinking about edge cases)
- Clean use of `enumerate()` and unpacking throughout
- Already thinking in tests — uses `assert` over `print`, writes edge cases unprompted
- Fixes bugs quickly and cleanly when pointed out

**Watch out for:**
- Using built-in names as variables (`list`, `dict`) — shadows Python built-ins
- `range(0, 10)` with `i+1` inside — prefer `range(1, 11)` for clarity
- PEP 8 spacing: no space before `:`, spaces inside tuple destructuring `(k, v)`
- Side effects inside functions (e.g. `helper.lesson()` inside `fizzbuzz()`)
- `if x in dict.keys()` → prefer `if x in dict`

---

*This file is updated as lessons are completed. See Syllabus.md for full progress tracking.*
