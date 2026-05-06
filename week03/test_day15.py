"""Tests for Day 15 — Practice + Mocking Basics"""
from unittest.mock import MagicMock, patch

import pytest

from day15_practice import *

from unittest.mock import mock_open


def test_add():
    actual_todos = _convert_to_todos(
        expected_todo_vals := [(False, "Item 1"), (False, "Item 2"), (False, "Item 3")])

    _assert_todos(expected_todo_vals, actual_todos)


def test_add_errors():
    actual_todos = []

    with pytest.raises(ValueError, match="Todo text is None or Empty"):
        add(actual_todos, "")

    with pytest.raises(ValueError, match="Todo text is None or Empty"):
        add(actual_todos, None)

    with pytest.raises(ValueError, match="Todo list cannot be None"):
        add(None, "Hello")


def test_list_todos():
    test_todos = _convert_to_todos(
        expected_todo_vals := [(False, "Item 1"), (False, "Item 2"), (False, "Item 3")])

    _assert_todos(expected_todo_vals, test_todos)


def test_list_todos_empty():
    _assert_todos([], list_todos([]))


def test_list_todos_error():
    with pytest.raises(ValueError, match="Todo list cannot be None"):
        list_todos(None)


def test_delete_todo():
    test_todos = _convert_to_todos([(False, "Item 1"), (False, "Item 2"), (False, "Item 3")])

    removed = delete_todo(test_todos, 1)

    assert removed.text == "Item 2"

    _assert_todos([(False, "Item 1"), (False, "Item 3")], test_todos)

    removed = delete_todo(test_todos, 1)

    assert removed.text == "Item 3"

    _assert_todos([(False, "Item 1")], test_todos)

    removed = delete_todo(test_todos, 0)

    assert removed.text == "Item 1"

    _assert_todos([], test_todos)


def test_delete_todo_errors():
    test_todos = _convert_to_todos([(False, "Item 1"), (False, "Item 2"), (False, "Item 3")])

    with pytest.raises(IndexError):
        delete_todo(test_todos, -1)

    with pytest.raises(IndexError):
        delete_todo(test_todos, 3)

    with pytest.raises(IndexError):
        delete_todo(test_todos, None)

    with pytest.raises(ValueError):
        delete_todo(None, 1)

    with pytest.raises(IndexError):
        delete_todo([], 1)


def _convert_to_todos(expected_vals: list[tuple[bool, str]]):
    converted = []
    for exp in expected_vals:
        add(converted, exp[1])
    return converted


def _assert_todos(expected_vals: list[tuple[bool, str]], actual_todos: list[Todo]):
    assert len(actual_todos) == len(expected_vals)
    for idx, actual_todo in enumerate(actual_todos):
        exp_done, exp_txt = expected_vals[idx]
        assert actual_todo.text == exp_txt
        assert actual_todo.done == exp_done


# Exercise: Add test_mock_storage to test_day15.py:
#
# Create a MagicMock() named mock_storage
# Set mock_storage.load.return_value = []
# Call mock_storage.load() and assert the return is []
# Assert mock_storage.load was called exactly once
# Call mock_storage.save("Buy milk") then assert it was called once with "Buy milk"
def test_mock_storage():
    mock_storage = MagicMock()

    mock_storage.load.return_value = []

    result = mock_storage.load()

    assert result == []

    mock_storage.save("Buy Milk")

    mock_storage.load.assert_called_once()

    mock_storage.save.assert_called_with("Buy Milk")

    mock_storage.save.assert_called_once_with("Buy Milk")

    assert mock_storage.save.call_count == 1

# Exercise: Write test_todo_uses_uuid in test_day15.py:
#
# Use @patch to replace uuid.uuid4 inside day15_practice
# Set return_value to a fixed string like "test-uuid-123"
# Create a Todo("Buy milk")
# Assert todo._id == "test-uuid-123"
# Assert the mock was called once

def test_todo_uses_uuid():
    with patch("day15_practice.uuid.uuid4") as mock_uuid:
        mock_uuid.return_value = "test-uuid-123"
        todo = Todo("Buy milk")
        assert todo._id == "test-uuid-123"
        mock_uuid.assert_called_once()

# write test_save_todo that:
#
# Creates a MagicMock() for storage
# Creates a real Todo
# Calls save_todo(storage, todo)
# Asserts storage.save was called once with the todo's text

def test_save_todo():
    storage = MagicMock()
    todo = Todo("Buy Milk")
    save_todo(storage, todo)
    storage.save.assert_called_once_with("Buy Milk")


def test_load_todos_from_file_real():
    from pathlib import Path
    filepath = Path(__file__).parent / "data" / "todos.txt"
    todos = load_todos_from_file(filepath)
    assert len(todos) == 4


# Exercise: Add load_todos_from_file(filepath) to day15_practice.py:
#
# Opens filepath and reads lines
# Returns a list of Todo objects, one per non-empty stripped line
#
# Then write test_load_todos_from_file using mock_open:

def test_load_todos_from_file_mocked():
    mock_data = "Buy milk\nDo laundry\n"

    with patch("builtins.open", mock_open(read_data=mock_data)) as mocked:
        result = load_todos_from_file("mock_file.txt")
        _assert_todos([(False, "Buy milk"), (False, "Do laundry")], result)

