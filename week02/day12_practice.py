"""Day 12 — Modules & Packages"""

# Import a specific constant.
from math import pi

# Import square root function
from math import sqrt

# Import ceil function as an alias.
from math import ceil as ceiling

# Import the math module and use math.pi  in a function circle_area(r)
# that returns the area of a circle
def circle_area(r):
    return pi * r ** 2


# Import the math module and use  math.sqrt() in a function hypotenuse(a,b)
# that returns the hypotenuse give two adjacent sides of a right triangle
def hypotenuse(a, b):
    return sqrt(a ** 2 + b ** 2)


# Import ceil from math using an alias ceiling and use it in a function round_up(n)
# that returns ceiling(n)
def round_up(n):
    return ceiling(n)



if __name__ == "__main__":
    print(f"Circle area = {circle_area(5)}")
    print(f"Hypotenuse = {hypotenuse(3, 4)}")
    print(f"Round Up = {round_up(2.3)}")