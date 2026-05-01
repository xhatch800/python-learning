"""Day 8 — Pythonic Idioms & Java Developer Gotchas"""


# Easy swap without temp variable.
def swap(a, b):
    a, b = b, a
    return a, b


# Exercise: Write a function is_valid_port(n) that returns True if n is
# a valid port number (1–65535, inclusive) — using a chained comparison.
# One line in the body.

def is_valid_port(n):
    return 1 <= n <= 65535


# Write a function classify(n) that returns "positive", "negative", or "zero" —
# using ternary expressions only (no if/elif block).

def classify(n):
    return (
        "zero" if n == 0 else
        "negative" if n < 0 else
        "positive"
    )


# Given nums = [10, 20, 30, 40, 50],
# unpack it so you have first, middle, and last as separate variables.
# Then print all three. One line of unpacking.

def splat_unpack_middle(n):
    first, *middle, last = n
    return first, middle, last


# Other splat unpack variations

def splat_unpack_first(n):
    *first, middle, last = n
    return first, middle, last


def splat_unpack_last(n):
    first, middle, *last = n
    return first, middle, last


def merge_collections(a, b):
    return [*a, *b]


def merge_dictionaries(a, b):
    return {**a, **b}


def multi_param_function(name, age, department):
    return f"Hello, {name} aged {age}. Your department is {department}."


# You have this tuple: record = ("Tony", "Engineer", "Anthropic", 2024).
# Unpack it so you capture only the name and year, discarding the middle two values.

def name_year_only(t):
    name, _, _, year = t
    return name, year


# Write a function summarize(items) that prints "Got items" if the list is non-empty,
# and "Nothing here" if it's empty — using truthiness, no len().

def summarize(items):
    return "Got items" if items else "Nothing here"


# Write a broken version of add_tag(tag, tags=[]) that demonstrates the bug,
# then write a fixed version add_tag_safe(tag, tags=None).
# Add both to day08_practice.py.

def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags


def add_tag_safe(tag, tags=None):
    if tags is None: tags = []
    tags.append(tag)
    return tags


# write a snippet that demonstrates == vs is on two lists with the same values.
# Use assert to show that == passes but is fails

def identity_gotchas():
    ## == value check, "is" object reference check.
    x = [1, 2, 3]
    y = [1, 2, 3]
    assert (x == y) == True
    assert (x is y) == False

    ## Exceptions: where "is" can be used because Python caches them.
    a = 256
    b = 256
    assert (a is b) == True


# Exercise: Write a function divide(a, b) that returns a tuple
# of (float_result, floor_result) for any two integers.
# Test with (7, 2) and (-7, 2) and assert the expected values.

def divide(a, b):
    return (a / b), (a // b)


def none_concept():
    assert not (None == 0)
    assert not (None == False)
    assert not (None == "")


# Write a function safe_double(n) that doubles n if it's not None,
# otherwise returns None. Use is None explicitly.
# Test with 0, 5, and None — make sure safe_double(0) returns 0, not None.

def safe_double(n):
    if n is None:
        return None

    return n * 2
