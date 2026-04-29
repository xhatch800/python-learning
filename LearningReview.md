# Tony's Python Learning Review

**Days completed: 1–5 | Environment: Python 3.14, IntelliJ**
**Last updated: 2026-04-29**

---

## Day 1 — Hello World
- Ran first Python script, understood no `main()`, no semicolons, no braces

## Day 2 — Variables & Types
- Dynamic typing, multiple assignment (`x, y, z = 1, 2, 3`), chained assignment (`a = b = 12`)
- `type()`, f-strings with formatting (`{gas_price:.2f}`)

## Day 3 — Control Flow
- `if/elif/else`, `for` with `enumerate()`, `range()` with step, `while`, `match` (Python 3.10+ switch)
- Notably explored `match` with guard conditions (`case val if val >= 90`) — beyond the lesson scope

## Day 4 — Functions
- `def`, default args, keyword args, `*args` (tuple), `**kwargs` (dict)
- Built a real SQL query builder with `build_query(table, **filters)` — strong backend instinct

## Day 5 — Collections
- `list`: slicing, stack (`append`/`pop`), queue (`deque`/`popleft`)
- `tuple`: unpacking, `enumerate()`
- `dict`: CRUD, `get()` with default, `items()` iteration, `del`
- `set`: `add`, `discard`, membership (`in`), set operations (`&`, `|`, `-`)
- List comprehensions: filtering, transforming, calling functions inside comprehensions

---

## Pythonic Idioms Picked Up Along the Way

| Idiom | Notes |
|---|---|
| Tuple unpacking | `x, y = point` |
| `enumerate()` on any iterable | replaces manual index tracking |
| Negative indexing | `[-1]` last, `[-2:]` last two |
| Slicing | start inclusive, end exclusive — same as Java's `subList` |
| `in` for membership checks | replaces `.contains()` |
| `deque` for efficient queues | `list.pop(0)` is O(n); `deque.popleft()` is O(1) |
| `Decimal("0.1")` for precision | like `BigDecimal` — always pass as string |
| Nested quotes in f-strings | works in Python 3.12+; breaks on older runtimes |

---

## Observations & Habits to Watch

**Strengths:**
- Extending exercises beyond requirements (SQL builder, composer filter, `match` statements)
- Good data structure instincts from Java background (choosing `deque` over list for queues)
- Clean use of `enumerate()` and unpacking throughout

**Watch out for:**
- Using built-in names as variables (`list`, `dict`) — shadows Python built-ins
- `range(0, 10)` with `i+1` inside — prefer `range(1, 11)` for clarity
- PEP 8 spacing: no space before `:` in `if i == 0 :`, spaces inside tuple destructuring `(k, v)`

---

*This file is updated as lessons are completed. See Syllabus.md for full progress tracking.*
