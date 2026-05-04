"""Tests for Day 14 — Functional Python."""
import pytest

from day14_practice import *
from functools import partial
import re


def test_apply_pipeline():
    assert apply_pipeline("  the quick brown fox   ",
                          [
                              str.upper,
                              str.strip,
                              lambda s: s.replace(" ", "-")
                          ]) == "THE-QUICK-BROWN-FOX"


def test_make_multiplier():
    triple = make_multiplier(3)
    assert triple(5) == 15
    assert triple(10) == 30


def test_product():
    assert product([1, 2, 3, 4]) == 1 * 2 * 3 * 4
    assert product([2, 3, 4]) == 24
    assert product([1, 5, 6]) == 30


def test_partials():
    square = partial(power, exp=2)
    cube = partial(power, exp=3)

    assert square(5) == 25
    assert square(4) == 16
    assert cube(2) == 8
    assert cube(5) == 125


def test_timer_slow_add(capsys):
    assert slow_add(2, 3) == 5
    printed = capsys.readouterr()
    assert printed.out.startswith("FunctionTimer(fn=slow_add,elapsedMsSec=0.1")


def test_single_dispatch_method_overloading():
    assert process(5) == 10
    assert process("10") == "Value is 10"
    assert process(["a","b","c"]) == "abc"
    assert process(None) == "womp womp"
