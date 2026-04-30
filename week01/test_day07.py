from day07_practice import *


def test_fizzbuzz():
    printable, fizzes, buzzes, fizzbuzzes = fizzbuzz(30)

    print(printable)
    assert fizzes == [3, 6, 9, 12, 18, 21, 24, 27]
    assert buzzes == [5, 10, 20, 25]
    assert fizzbuzzes == [15, 30]


def test_fizzbuzz_zero_input():
    printable, fizzes, buzzes, fizzbuzzes = fizzbuzz(0)
    print(printable)
    assert fizzes == []
    assert buzzes == []
    assert fizzbuzzes == []


def test_reverse_str():
    assert reverse_str("practice") == "ecitcarp"


def test_reverse_str_none():
    assert reverse_str(None) is None


def test_word_freq_counter():
    sentence = """
        The fast cat   fast cat ran   ; but 
        the slow cat slow cat slow cat stayed behind, 
        behind the old wooden fence.
    """

    dictionary = word_freq_counter(sentence)

    assert dictionary == {
        'BEHIND': 2,
        'BUT': 1,
        'CAT': 5,
        'FAST': 2,
        'FENCE': 1,
        'OLD': 1,
        'RAN': 1,
        'SLOW': 3,
        'STAYED': 1,
        'THE': 3,
        'WOODEN': 1
    }


def test_word_freq_counter_none():
    actual = word_freq_counter(None)
    assert len(actual) == 0
