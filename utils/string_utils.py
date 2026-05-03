"""String Utils"""

# Create utils/string_utils.py with one function: slugify(text) —
# lowercases the text and replaces spaces with hyphens
# (e.g. "Hello World" → "hello-world")

def slugify(text):
    if not text:
        raise ValueError("Text is empty.")

    if not isinstance(text, str):
        raise TypeError("Text must be a string")

    return text.lower().replace(" ", "-")