"""Tests for Day 10 — File I/O"""
from day10_practice import *


def test_write_read_lines():
    temp_file = "tmp/tmp.test_day10.testfile01.txt"
    lines = ["apple", "banana", "oranges"]
    write_lines(temp_file, lines)
    actual = read_lines(temp_file)
    assert actual == lines


def test_write_read_csv():
    temp_file = "tmp/tmp.test_day10.testfile02.txt"
    rows = [
        {"name": "John", "age": "32", "city": "Minneapolis"},
        {"name": "Susan", "age": "53", "city": "New York"},
        {"name": "Blair", "age": "45", "city": "Los Angeles"}
    ]
    write_csv(temp_file, rows)
    actual = read_csv(temp_file)
    assert actual == rows
