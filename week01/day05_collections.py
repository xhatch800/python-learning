# lists

fruits = ["apple", "banana", "orange", "strawberry"]
print(f"List: fruits: {fruits}")

a, b, c, d = fruits

print(f"List: unpack: {a}, {b}, {c}, {d}")
fruits.append("dragonfruit")

print(f"List: add dragonfruit: {fruits}")

fruits.remove("banana")

print(f"List: remove banana: {fruits}")

print(f"List: First element: {fruits[0]}")

print(f"List: Last element: {fruits[-1]}")

print(f"List: first 3 {fruits[:3]}")

print(f"List: last 3 to end {fruits[-3:]}")

print(f"List: index 1 to 2 {fruits[1:3]}")

print(f"List: start at beginning until 3rd from last: {fruits[:-3]}")

# List as a stack
stack = []

stack.append(10)

stack.append(30)

print(f"Stack: stack={stack}")
popped = stack.pop()
print(f"Stack: popped={popped}, stack={stack}")

# List as a queue
from collections import deque

queue = deque()

queue.append(10)

queue.append(30)

print(f"Queue: queue={queue}")
dequed = queue.popleft()
print(f"Queue: dequed={dequed}, queue={queue}")

# tuple

point = (10, 29)

print(f"Tuple: tuple {point}")

for i, item in enumerate(point):
    print(f" point {i} = {item} ")

x, y = point

print(f"Tuple: x = {x}, y = {y}")

# dictionary

user = {"name": "Tony", "role": "admin", "age": 30}

print(f"Dict:  user = {user}")
print(f"Dict: {user["name"]}, {user["role"]}, {user["age"]}")

user["department"] = "IT Services"

print(f"Dict:  added department user = {user}")

for i, (k, v) in enumerate(user.items()):
    print(f" {k} = {v}")

del user["department"]

print(f"Dict:  removed department - user = {user}")

# Sets

roles = {"admin", "viewer", "editor"}

print(f"Sets: roles={roles}")
roles.add("owner")
roles.discard("viewer")  # remove if exists — no KeyError

print(f"Sets: roles={roles}")

roles.add("owner")
print(f"Sets: reinsert owner.  roles={roles}")
print(f"Sets: check admin = {"admin" in roles}")
print(f"Sets: check viewer = {"viewer" in roles}")

# set ops
k = {1, 2, 3}
m = {2, 3, 4}
print(f"intersect {k & m}")
print(f"union {k | m}")
print(f"diff {k - m}")

# list comprehension
def complement(comp):
    return "The GREAT "+comp.upper()

complist = ["vivaldi", "mozart", "beethoven", "debussy"]

print(f"{ [composer.capitalize() for composer in complist] }")
print(f"{ [composer.upper() for composer in complist if composer[0].upper() == "M"] }")
print(f"{ [complement(composer) for composer in complist if composer[0].upper() == "M"] }")

# Exercises:

# A list of 5 numbers — find the max, min, and sum without using a loop

list_of_nums = [12, 34, 10, 55, 4]
print(f"max = {max(list_of_nums)}")
print(f"min = {min(list_of_nums)}")
print(f"sum = {sum(list_of_nums)}")

# A dict representing a product (name, price, in_stock) — safely get a "discount" key with a default of 0

product = {
    "name": "Ipad",
    "price": 599.99,
    "in_stock": True
}

print(f"Discount {product.get("discount", 0.0)}")

# A set of tags — add one, remove one, check membership

tags = {"Gold", "Premier"}

tags.add("Legacy")
tags.remove("Gold")

print(f"Tags: {tags}")
print(f"Gold ? {"Gold" in tags}")
print(f"Gold ? {"Legacy" in tags}")

# A list comprehension that filters even numbers and squares them from a list of 1–10

result = [(i+1)**2 for i in range(0, 10) if (i+1) % 2 == 0]

print(f"{result}")
