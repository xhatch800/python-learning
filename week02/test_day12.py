"""Tests for Day 12 — Modules & Packages"""
import pytest

from day12_practice import round_up, hypotenuse, circle_area
from math import pi
from utils.string_utils import slugify


def test_circle_area():
    assert round(circle_area(2), 4) == 12.5664


def test_hypotenuse():
    assert hypotenuse(3, 4) == 5


def test_round_up():
    assert round_up(pi) == 4


def test_slugify():
    assert slugify("Hello World") == "hello-world"

    with pytest.raises(ValueError):
        slugify("")

    with pytest.raises(ValueError):
        slugify(None)

    with pytest.raises(TypeError):
        slugify(120)


