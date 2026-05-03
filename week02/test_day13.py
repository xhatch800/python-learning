"""Tests for Day 13 — OOP in Python"""
import pytest

from day13_practice import Product, DiscountedProduct, FlatDiscount, PercentDiscount, Category


def test_product():
    product = Product("Sony Headphones", 329.99)

    product.apply_discount(20)

    print(f"\nPrice of product {product.name} is {product.price}")
    assert product.price == 263.99


def test_product_equality():
    p1 = Product("Sony Headphones", 329.99)
    p2 = Product("Sony Headphones", 329.99)

    assert p1 is not p2
    assert p1 == p2


def test_product_inequality():
    p1 = Product("Sony Headphones", 329.99)
    p1_diff_name = Product("Sony Playstation", 329.99)
    p1_diff_price = Product("Sony Headphones", 329.44)

    assert p1 != p1_diff_name
    assert p1 != p1_diff_price


def test_product_hash():
    p1 = Product("Sony Headphones", 329.99)
    p1_copy = Product("Sony Headphones", 329.99)

    assert hash(p1) == hash(p1_copy)


def test_product_prints():
    p1 = Product("Sony Headphones", 329.99)

    print(p1)

    assert str(p1) == "Product Sony Headphones is priced at 329.99"
    assert repr(p1) == "Product(name=Sony Headphones, price=329.99)"


def test_bad_price_setting():
    p1 = Product("Sony Headphones", 329.99)

    with pytest.raises(ValueError):
        p1.price = -12

    with pytest.raises(ValueError):
        p1.price = None

    with pytest.raises(ValueError):
        bad = Product("foo", -100)


def test_discounted_product():
    regular = Product("Sony Headphones", 400)
    digital = DiscountedProduct("Super Mario Brothers", 15)

    regular.apply_discount(70)
    digital.apply_discount(70)

    assert regular.price == 120  # 70% discount applied
    assert digital.price == 7.5  # only 50% discount applied because of cap


def test_percent_discount():
    discount = PercentDiscount("May Sale Discount", 30)

    assert discount.apply(100) == 70


def test_flat_discount():
    discount = FlatDiscount("May Sale Discount", 12)

    assert discount.apply(100) == 88

    assert discount.apply(5) == 5


def test_category_enum():
    assert Category.ELECTRONICS.display_name == "Electronics"
    assert Category.KITCHEN.display_name == "Kitchen"
    assert Category.OFFICE.display_name == "Office"

    assert list(Category) == [Category.ELECTRONICS, Category.KITCHEN, Category.OFFICE]



