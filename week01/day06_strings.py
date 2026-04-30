from utils import helper

helper.lesson("Slicing Recap")

s = "hello world"

assert s[0] == "h"
assert s[-1] == "d"
assert s[0:5] == "hello"
assert s[6:] == "world"
assert s[::-1] == "dlrow olleh"
assert s[::1] == "hello world"  # step +1, left to right (default)
assert s[::2] == "hlowrd"  # "bced"     — every 2nd character

helper.lesson("Common Methods")

s = "  hello world  "

assert s.strip() == "hello world"
assert s.lstrip() == "hello world  "
assert s.rstrip() == "  hello world"

assert s.upper() == "  HELLO WORLD  "
assert s.lower() == "  hello world  "
assert s.strip().capitalize() == "Hello world"
assert s.title() == "  Hello World  "

assert s.replace("world", "python") == "  hello python  "

assert s.split() == ["hello", "world"]
assert "hello, world".split(",") == ["hello", " world"]

assert " | ".join(["a", "b", "c"]) == "a | b | c"

helper.lesson("Membership and Search")
s = "hello world"

assert "world" in s
assert s.startswith("hello")
assert s.endswith("world")
assert s.find("world") == 6
assert s.count("l") == 3

helper.lesson("Multi-line Strings")

query = """
        SELECT *
        FROM users
        WHERE active = true \
        """

print(query)

helper.lesson("Formatting")

name, age = "Tony", 30

assert f"Hello {name}, age {age}" == "Hello Tony, age 30"  # USE THIS!
assert "Hello {}, age {}".format(name, age) == "Hello Tony, age 30"  # OLDER way...
assert "Hello %s, age %d" % (name, age) == "Hello Tony, age 30"  # % OLDEST, avoid

# Your turn: Create week01/day06_strings.py and write:
#
# Take a messy string "  python is GREAT  " — strip it, lowercase it, then title-case it
# Split "apple,banana,orange" into a list, then join it back with |
# Check if "world" is in "hello world" and print the index where it starts
# Write a multi-line f-string that acts as a mini user profile (name, role, joined date)
# Reverse the string "backend" using slicing

helper.lesson("Exercise 1")

assert "  python is GREAT  ".strip().lower().title() == "Python Is Great"

helper.lesson("Exercise 2")

assert "|".join("apple,banana,orange".split(",")) == "apple|banana|orange"

helper.lesson("Exercise 3")

# Walrus operator!
print(f"Found at {i}" if (i := s.find("world")) > -1 else "Missing")

helper.lesson("Exercise 4")

name, role, joined = "Tony", "Developer", "2025/02/25"
multiline = f"""
Name: {name}
Role: {role}
Joined: {joined}
"""

print(multiline)

helper.lesson("Exercise 5")

assert "backend"[::-1] == "dnekcab"


helper.lesson("Translation")

# Build a translation table — map characters to replacements
table = str.maketrans("aeiou", "AEIOU")   # replace vowels with uppercase
assert "hello world".translate(table) == "hEllO wOrld"

# Can also delete characters
table = str.maketrans("", "", "aeiou")    # delete all vowels
assert "hello world".translate(table)  == "hll wrld"

