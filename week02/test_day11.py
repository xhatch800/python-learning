"""Tests for Day 11 — Error Handling"""
import pytest

from day11_practice import *


def test_safe_divide():
    result = 0 / 1
    assert safe_divide(15, 2) == 7.5
    assert safe_divide(15, 0) is None
    assert safe_divide(0, 1) == 0.0
    assert safe_divide("a", 2) is None


def test_create_user():
    assert create_user("Tony", 53) == {"name": "Tony", "age": 53}
    assert create_user("Baby Tony", 0) == {"name": "Baby Tony", "age": 0}
    assert create_user("Really Old Tony", 150) == {"name": "Really Old Tony", "age": 150}

    # Name related exceptions...
    with pytest.raises(ValidationError):
        create_user("", 53)

    with pytest.raises(ValidationError):
        create_user("   ", 53)

    with pytest.raises(ValidationError):
        create_user(None, 53)

    # Age related exceptions
    with pytest.raises(TypeError):
        create_user("Tony", "53")

    with pytest.raises(ValidationError):
        create_user("Tony", -1)

    with pytest.raises(ValidationError):
        create_user("Tony", 151)


def test_find_users():
    users = [
        {"name": "John", "age": "32", "city": "Minneapolis"},
        {"name": "Susan", "age": "53", "city": "New York"},
        {"name": "Blair", "age": "45", "city": "Los Angeles"}
    ]

    assert find_users(users, "John") == {"name": "John", "age": "32", "city": "Minneapolis"}

    with pytest.raises(NotFoundError):
        find_users(users, "Evelyn")
