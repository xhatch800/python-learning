"""Tests for Day 9 — List Comprehensions & Generators"""

from day09_practice import *


def test_squares_of_evens():
    assert squares_of_evens([1, 2, 3, 4, 5, 6]) == [4, 16, 36]
    assert squares_of_evens([6, 13, 12]) == [36, 144]
    assert squares_of_evens([1, 3, 5]) == []
    assert squares_of_evens([]) == []
    assert squares_of_evens(None) is None


def test_flatten():
    assert (
            flatten([[1, 2], [3, 4], [5, 6]])
            == [1, 2, 3, 4, 5, 6]
    )

    assert flatten([]) == []
    assert flatten(None) is None


def test_word_lengths():
    assert word_lengths(["apple", "bananas", "oranges"]) == {
        "apple": 5,
        "bananas": 7,
        "oranges": 7
    }

    assert word_lengths([]) == {}

    assert word_lengths(None) is None

    assert word_lengths([None, "apple"]) == {"apple": 5}


def test_first_n_squares():
    assert list(first_n_squares(5)) == [0, 1, 4, 9, 16]


def test_big_sum():
    assert big_sum(10) == 45


def test_pair_up():
    assert pair_up(["anna", "john"], ["karenina", "smith"]) == {
        "anna": "karenina",
        "john": "smith"
    }


def test_apply_all():
    assert apply_all(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]


def test_keep_if():
    assert keep_if(lambda x: x > 5, [1, 5, 2, 20, 6]) == [20, 6]


def test_sort_by_length():
    assert sort_by_length(["banana", "orange", "apple"]) == ["apple", "banana", "orange"]


def test_sort_people():
    assert sort_people([
        ("Joe", 30),
        ("Anthony", 53)
    ]) == [
        ("Anthony", 53),
        ("Joe", 30)
    ]
