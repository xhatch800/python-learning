"""Day 15 — Practice + Mocking Basics

Topics: CLI app (to-do manager), pytest mocking with unittest.mock
"""
import sys
import uuid

# Exercise: Implement add_todo(todos, text), list_todos(todos), and delete_todo(todos, index)
# as standalone functions in day15_practice.py.
# These are the pure-logic functions — separate from the main() loop so they're testable.
class Todo:
    def __init__(self, text):
        super().__init__()
        self._id = str(uuid.uuid4())
        self._text = text
        self._done = False

    @property
    def text(self):
        return self._text

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, val):
        self._done = val

    def __eq__(self, value, /):
        if not isinstance(value, Todo):
            return NotImplemented
        return self._id == value._id

    def __hash__(self):
        return hash(self._id)

    def __str__(self):
        return f"[{'X' if self.done else ' '}]  {self.text} (id={self._id})"

    def __repr__(self):
        return f"Todo(id={self._id}, text={self.text}', done={self.done})"


def add(todos: list[Todo], text: str):
    _assert_todo_contents(todos)
    if not text:
        raise ValueError("Todo text is None or Empty")
    todos.append(Todo(text))


def list_todos(todos: list[Todo]) -> list[Todo]:
    _assert_todo_contents(todos)
    return list(todos)


def delete_todo(todos: list[Todo], index):
    _assert_todo_contents(todos)
    if index is None or index >= len(todos) or index < 0:
        raise IndexError(f"Index {index} is invalid.  Todo size is {len(todos)}.")
    removed = todos.pop(index)
    return removed


def set_todo_status(todos: list[Todo], index, status=True):
    _assert_todo_contents(todos)
    if index is None or index >= len(todos) or index < 0:
        raise IndexError(f"Index {index} is invalid.  Todo size is {len(todos)}.")
    todos[index].done = status

def show_todos(todos: list[Todo]):
    for idx, t in enumerate(list_todos(todos)):
        print(f"{idx:2d}. {t}")

def _assert_todo_contents(todos: list[Todo]):
    if todos is None:
        raise ValueError("Todo list cannot be None")

# Exercise: Add save_todo(storage, todo) to day15_practice.py:
#
# Takes a storage object and a Todo
# Calls storage.save(todo.text)

def save_todo(storage, todo:Todo):
    storage.save(todo.text)


def load_todos_from_file(filepath):
    with open(filepath, "r") as f:
        return [Todo(line.strip("\n").strip())
                for line in f.readlines() if line.strip("\n").strip()]


def main():
    todos = []
    while True:
        cmd = input("> ").strip()

        if cmd.lower().startswith(add_prefix := "add "):
            txt = cmd.removeprefix(add_prefix)
            if txt:
                add(todos, txt)
                print(f"Todo item added: {txt}")
            else:
                print("Usage: add <text>")
        elif cmd.lower() in ["list", "show"]:
            if not todos:
                print("No todos found.")
            show_todos(todos)
        elif cmd.lower().startswith(done_prefix := "done "):
            try:
                idx = int(cmd.removeprefix(done_prefix))
            except (ValueError, IndexError):
                print("Usage: done <idx = valid index>")
            else:
                try:
                    set_todo_status(todos, idx, True)
                except IndexError:
                    print("Invalid index. Usage: done <idx = valid index>")
                else:
                    show_todos(todos)
        elif cmd.lower().startswith(done_prefix := "delete "):
            try:
                idx = int(cmd.removeprefix(done_prefix))
            except ValueError:
                print("Usage: delete <idx = valid index>")
            else:
                try:
                    removed = delete_todo(todos, idx)
                except IndexError:
                    print("Invalid index. Usage: delete <idx = valid index>")
                else:
                    print(f"Todo removed: {removed}")
        elif cmd.lower() in ["exit", "quit"]:
            sys.exit(0)
        else:
            print(f"Unknown command '{cmd}'.  Try again.")


if __name__ == "__main__":
    main()
