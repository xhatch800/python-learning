# Parking Lot Questions and Points

- [x] Array and Set equality check — Answered Day 7: list `==` is order-sensitive; set `==` is value-only (like ArrayList vs HashSet in Java)
- [x] String maketrans and translate — Answered Day 7: `str.maketrans()` builds a char mapping table; `.translate()` applies it — bulk character replacement/deletion
- [x] s[::-1] what is this? — Answered Day 6: slice step notation; `[::-1]` traverses string backwards
- [x] Comparators in Java → covered Day 9: `sorted(key=...)`, multi-key tuples, negate for descending
- [x] Priority Queues → deferred to Day 16–17 (heapq in standard library)
- [x] Regular expressions → already in Syllabus Day 16–17 (re module)
- [x] Virtual environments, requirements.txt, and how IDEs (IntelliJ/PyCharm) auto-detect and install dependencies → covered Day 7, deep dive in Day 12
- [x] Functional overriding and overloading → deferred to Day 13 (overriding) and Day 14 (overloading alternatives)
- [ ] Deep dive on GIL (Global Interpreter Lock) — limitations, implications for enterprise/high-scalability apps, and Python's concurrency answers → deferred to Day 20–21
- [x] Dunder methods (`__eq__`, `__hash__`, `__str__`, `__repr__`) — Answered Day 13: define inside class body; `__eq__` → `equals()`, `__hash__` → `hashCode()`, `__str__` → `toString()`, `__repr__` → developer-facing string; return `NotImplemented` (not raise) when types don't match
- [x] Enums in Python — Answered Day 13: `class Foo(Enum)`, values can be int/string/auto(); `.name`, `.value`, iterable; `@property` works inside enum body; string values can serve as display names directly
- [ ] Passing functions as parameters — first-class functions in Python → deferred to Day 14 (Functional Python)
- [x] Java Optional vs Python equivalent — Answered Day 11: Python returns `None` for absence or raises exceptions for invalid state; `Optional[str]` from `typing` is type-hint documentation only, no runtime enforcement
- [ ] Type hints on lambdas — lambdas can't be annotated; use named functions when types matter → deferred to Day 14 (Functional Python)
- [ ] pandas for typed CSV processing — `pd.read_csv()` with `dtype=` for schema-aware CSV handling; relevant for data pipelines → defer until needed
- [x] Casting in Python — Answered Day 11: no casting in Java sense; `int()`, `float()`, `str()` are constructor calls that convert values; raise `ValueError` on failure, `TypeError` on wrong type
- [x] Python has no `final` for parameters — Answered Day 13: no enforcement; convention is don't reassign params; `Final` from `typing` is for class-level constants only; use immutable types (`tuple`, frozen dataclass) for true immutability
