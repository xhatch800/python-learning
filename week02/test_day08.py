"""Tests for Day 8 — Pythonic Idioms & Java Developer Gotchas"""
from day08_practice import *


def test_swap():
    a, b = 1, 2

    assert a == 1
    assert b == 2

    a, b = swap(a, b)

    assert a == 2
    assert b == 1


def test_is_valid_port():
    assert is_valid_port(0) == False
    assert is_valid_port(1) == True
    assert is_valid_port(8000) == True
    assert is_valid_port(65535) == True
    assert is_valid_port(65536) == False


def test_classify():
    assert classify(-1) == "negative"
    assert classify(0) == "zero"
    assert classify(1) == "positive"


def test_splat_unpack_middle():
    first, middle, last = splat_unpack_middle([10, 20, 30, 40, 50])
    assert first == 10
    assert last == 50
    assert middle == [20, 30, 40]


def test_splat_unpack_first():
    first, middle, last = splat_unpack_first([10, 20, 30, 40, 50])
    assert first == [10, 20, 30]
    assert last == 50
    assert middle == 40


def test_splat_unpack_last():
    first, middle, last = splat_unpack_last([10, 20, 30, 40, 50])
    assert first == 10
    assert last == [30, 40, 50]
    assert middle == 20


def test_merge_collections():
    a = [10, 20, 30]
    b = [40, 50]
    assert merge_collections(a, b) == [10, 20, 30, 40, 50]


def test_merge_dictionaries():
    a = {"name": "Tony"}
    b = {"age": 53}
    assert merge_dictionaries(a, b) == {
        "name": "Tony",
        "age": 53
    }


def test_multi_param_using_dict():
    d = {
        "name": "Tony",
        "age": 53,
        "department": "sales"
    }

    assert multi_param_function(**d) \
           == "Hello, Tony aged 53. Your department is sales."


def test_name_year_only():
    record = ("Tony", "Engineer", "Anthropic", 2024)
    assert name_year_only(record) == ("Tony", 2024)


def test_truthiness_idioms():
    # Falsy — evaluate to False
    assert not []
    assert not {}
    assert not ()
    assert not ""
    assert not 0
    assert not None

    # Truthy — everything else
    assert [1, 2]
    assert {"a": 1}
    assert "hello"
    assert 42


def test_summarize():
    assert summarize(["abc", "def"]) == "Got items"
    assert summarize([]) == "Nothing here"
    assert summarize(None) == "Nothing here"


def test_add_tag_buggy():
    tags = add_tag("hey")
    assert tags == ["hey"]

    tags2 = add_tag("foo")
    assert tags2 == ["hey", "foo"]  # This is a bad side effect.  Param tags retained old calls value.


def test_add_tag_safe():
    tags = add_tag_safe("hey")
    assert tags == ["hey"]

    tags2 = add_tag_safe("foo")
    assert tags2 == ["foo"]  # This is a bad side effect.  Param tags retained old calls value.


def test_identity_gotchas():
    identity_gotchas()

def test_divide():
    assert divide(7, 2) == (3.5, 3)
    assert divide(-7, 2) == (-3.5, -4)

def test_none_concept():
    none_concept()

def test_safe_double():
    assert safe_double(0) == 0
    assert safe_double(5) == 10
    assert safe_double(None) is None

