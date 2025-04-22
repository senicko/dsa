from math import inf
from collections import deque


def bfs_list(graph, s):
    n = len(graph)
    queue = deque()

    # Initialize state arrays.
    visited = [False] * n
    parent = [None] * n
    distance = [inf] * n

    # Mark starting node as visited.
    visited[s] = True
    distance[s] = 0
    queue.appendleft(s)

    while queue:
        v = queue.pop()

        # For every neighbour of v.
        for u in graph[v]:
            # Skip it if it's already visited.
            if visited[u]:
                continue

            # Mark it as visited.
            visited[u] = True
            parent[u] = v
            distance[u] = distance[v] + 1
            queue.appendleft(u)

    return visited, distance, parent


def bfs_matrix(graph, s):
    n = len(graph)
    queue = deque()

    # Initialize state arrays.
    visited = [False] * n
    parent = [None] * n
    distance = [inf] * n

    # Mark starting node as visited.
    visited[s] = True
    distance[s] = 0
    queue.appendleft(s)

    while queue:
        v = queue.pop()

        # This for always makes O(V) iterations
        # making the algorithm run in O(V^2)
        # time regardless of graph's density.
        for u in range(n):
            if graph[v][u] != 1 or visited[u]:
                continue

            visited[u] = True
            parent[u] = v
            distance[u] = distance[v] + 1
            queue.appendleft(u)

    return visited, distance, parent


if __name__ == "__main__":
    graph_list = [
        [1, 4],
        [2],
        [3],
        [],
        [2]
    ]

    graph_matrix = [
        [0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]

    s = 0
    result_list = bfs_list(graph_list, s)
    result_matrix = bfs_matrix(graph_matrix, s)

    assert result_list == result_matrix
    print(result_list)
