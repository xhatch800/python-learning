import heapq


class Adjacency:
    def __init__(self, to_node: str, weight: int):
        self._to_node = to_node
        self._weight = weight

    @property
    def to_node(self):
        return self._to_node

    @property
    def weight(self):
        return self._weight


adjacency_list = {
    "A": [
        Adjacency("B", 1),
        Adjacency("C", 2)
    ],
    "B": [
        Adjacency("Z", 5)
    ],
    "C": [
        Adjacency("Z", 2)
    ]
}

start_node = "A"
end_node = "Z"

nodes = set(adjacency_list.keys()) | {x.to_node for adj_list in adjacency_list.values() for x in adj_list}
distances = {node: float("infinity") if node != start_node else 0 for node in nodes}

pq = []
prev_nodes = {}
heapq.heappush(pq, (0, start_node))

while pq:
    curr_best_dist, curr_best_node = heapq.heappop(pq)

    if curr_best_node == end_node:
        break

    for adjacent in adjacency_list[curr_best_node]:
        curr_adj_distance = adjacent.weight + curr_best_dist
        if curr_adj_distance < distances[adjacent.to_node]:
            distances[adjacent.to_node] = curr_adj_distance
            heapq.heappush(pq, (curr_adj_distance, adjacent.to_node))
            prev_nodes[adjacent.to_node] = curr_best_node

    # end for

# end while

# Get the best path by looking at backtracking nodes in prev_nodes.
curr = end_node
best_path = [curr]
while curr != start_node:
    curr = prev_nodes.get(curr)
    best_path.insert(0, curr)

print(f"Dijkstra Best Path : best_path={best_path}, total_cost={distances[end_node]}")
