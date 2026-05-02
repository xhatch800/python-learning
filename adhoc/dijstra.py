import heapq

pq = []

nodes = ["A", "B", "C"]

adjacency = {
    "A": [
        ("B", 1),
        ("C", 2)
    ],
    "B": [
        ("Z", 2)
    ],
    "C": [
        ("Z", 2)
    ]
}
