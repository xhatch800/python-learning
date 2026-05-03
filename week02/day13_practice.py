"""Day 13 — OOP in Python"""
from abc import ABC, abstractmethod
from enum import Enum, auto


# define a Product class with:
#
# name (str) and price (float) set in __init__
# A apply_discount(percent) method that reduces price by that percentage
# Instantiate one, apply a discount, and print the result

class Product:
    def __init__(self, name: str, price: float = 0.0):
        self.name = name
        self.price = price  # triggers setter validation which is good.

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value is None:
            raise ValueError("Price cannot be empty")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    def apply_discount(self, percent):
        self.price *= (1 - percent / 100)
        self.price = round(self.price, 2)

    def __str__(self):
        return f"Product {self.name} is priced at {self.price}"

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price

    def __hash__(self):
        return hash((self.name, self.price))


# Create a DiscountedProduct subclass of Product that:
#
# Takes an extra max_discount parameter in __init__ (e.g. 50 for 50%)
# Overrides apply_discount to cap the discount at max_discount, then delegates to super()
# Add a test that verifies the cap is enforced

class DiscountedProduct(Product):
    def __init__(self, name: str, price: float, max_discount: float = 50):
        super().__init__(name, price)
        self._max_discount = max_discount

    def apply_discount(self, percent):
        cap = min(percent, self._max_discount)
        super().apply_discount(cap)


# Exercise: Define an abstract class Discount with one @abstractmethod: apply(price: float) -> float.
# Then implement two concrete subclasses — PercentDiscount and FlatDiscount.
# Write a test that applies both to a price.

class Discount(ABC):
    def __init__(self, name: str, discount: float):
        self._name = name
        self._discount = discount

    @abstractmethod
    def apply(self, price: float) -> float:
        ...

    @property
    def discount(self):
        return self._discount

    @property
    def name(self):
        return self._name


class PercentDiscount(Discount):
    def __init__(self, name: str, discount: float):
        super().__init__(name, discount)

    def apply(self, price: float):
        return (1 - (self.discount / 100)) * price

    def __eq__(self, other):
        if not isinstance(other, PercentDiscount):
            return NotImplemented
        return self.name == other.name and self.discount == other.discount

    def __hash__(self):
        return hash(self.discount)

    def __repr__(self):
        return f"PercentDiscount(name={self.name},discount={self.discount})"

    def __str__(self):
        return f"Percent Discount {self.name} of  {self.discount})"


class FlatDiscount(Discount):
    def __init__(self, name: str, discount: float):
        super().__init__(name, discount)

    def apply(self, price: float):
        if self.discount > price:
            return price
        return price - self.discount

    def __eq__(self, other):
        if not isinstance(other, FlatDiscount):
            return NotImplemented
        return self.name == other.name and self.discount == other.discount

    def __hash__(self):
        return hash(self.discount)

    def __repr__(self):
        return f"FlatDiscount(name={self.name},discount={self.discount})"

    def __str__(self):
        return f"Flat Discount {self.name} of  {self.discount})"


# Exercise: Define a Category enum with at least 3 values using auto().
# Add a display_name property that returns a formatted string
# (e.g. "Electronics" instead of "ELECTRONICS").
# Write a test that checks the name, value, and display_name of one member.

class Category(Enum):
    ELECTRONICS = auto()
    KITCHEN = auto()
    OFFICE = auto()

    @property
    def display_name(self):
        return self._name_.capitalize()
