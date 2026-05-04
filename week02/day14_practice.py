"""Day 14 — Functional Python: first-class functions, lambda, functools, decorators."""

from functools import reduce, wraps, singledispatch
from time import perf_counter, sleep


# Write apply_pipeline(text, fns) — takes a string and a list of functions,
# applies them left to right, returns the final result. Keep the body to 1–2 lines.

def apply_pipeline(text, fns):
    for fn in fns:
        text = fn(text)
    return text


# Write make_multiplier(n) — a function that returns a lambda that multiplies its input by n.
# triple = make_multiplier(3)
# triple(5)   # 15
# triple(10)  # 30
# This is your first closure — n is captured from the outer scope.

def make_multiplier(n):
    return lambda x: x * n


# Using reduce, write product(nums) — returns the product of all numbers in a list.
# No loops, no math.prod.

def product(nums: list):
    return reduce(lambda acc, x: acc * x, nums, 1)


# Exercise: Using partial, create two pre-configured functions from this base:

def power(base, exp):
    return base ** exp


# Exercise: Write a @timer decorator that prints
# how long the decorated function took to run. Use time.perf_counter() for timing.

def timer(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        try:
            result = fn(*args, **kwargs)
        finally:
            stop = perf_counter()
            print(f"FunctionTimer(fn={fn.__name__},elapsedMsSec={stop - start})")
        return result

    return wrapper


@timer
def slow_add(a, b):
    sleep(0.1)
    return a + b

## Demonstrates method overloading using single dispatch

@singledispatch
def process(value):
    raise TypeError(f"Unsupported type {type(value)} for function {process.__name__}")

@process.register(int)
def _(value):
    return value * 2

@process.register(str)
def _(value):
    return f"Value is {value}"

@process.register(list)
def _(value):
    return reduce(lambda acc, x: acc + x, value)

@process.register(type(None))
def _(value):
    return "womp womp"

