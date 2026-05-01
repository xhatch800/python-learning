"""Day 9 — List Comprehensions & Generators"""


# squares_of_evens(nums) — returns a list of squares of even numbers from the input list

def squares_of_evens(nums):
    if nums is None: return None
    return [x ** 2 for x in nums if x % 2 == 0]


# flatten(matrix) — takes a list of lists and returns a single flat list

def flatten(matrix):
    if matrix is None: return None
    return [col for row in matrix for col in row]


# word_lengths(words) — returns a dict mapping each word → its length

def word_lengths(words):
    if words is None: return None
    return {word: len(word) for word in words if word}


# first_n_squares(n) — a generator function using yield that produces the squares of 0 through n-1

def first_n_squares(n):
    for sq in range(n):
        yield sq ** 2


# big_sum(limit) — returns the sum of all numbers from 0 to limit - 1 using a generator expression (no list, no explicit loop)

def big_sum(limit):
    return sum(n for n in range(limit))


# pair_up(keys, values) : uses zip() to return a dict from two lists

def pair_up(keys, values):
    return {k: v for k, v in zip(keys, values)}

# apply_all(fn, items) — uses map() to apply a function to every item, returns a list

def apply_all(fn, items):
    return list(map(fn, items))

# keep_if(predicate, items) — uses filter() to return only items where predicate is True

def keep_if(predicate, items):
    return list(filter(predicate, items))


# sort_by_length(words) sorts a list of strings by length (shortest first), no lambda

def sort_by_length(words):
    return sorted(words, key=len)

# sort_people(people) - given a list of (name, age) tuples, sort by age descending, then name alphabetically

def sort_people(people):
    return sorted(people, key = lambda p : (-p[1], p[0]))