from collections import deque
from math import inf


# Builds distance array to other vertices for vertex s.
def shortest_path_from(graph, s):
    n = len(graph)
    queue = deque()

    # State.
    distance = [inf] * n
    visited = [False] * n
    parents = [None] * n

    # Process starting vertex.
    distance[s] = 0
    visited[s] = True
    queue.appendleft(s)

    while queue:
        v = queue.pop()

        for u in graph[v]:
            if not visited[u]:
                parents[u] = v
                visited[u] = True
                distance[u] = distance[v] + 1
                queue.appendleft(u)

    return parents, distance


if __name__ == "__main__":
    graph = [
        [1, 6],
        [0, 2],
        [1, 3],
        [2, 4, 6],
        [3, 5],
        [4, 6],
        [5, 0, 3]
    ]

    parents, distances = shortest_path_from(graph, 0)

    # Print shortest path to vertex 4 from vertex 0
    end = 4
    curr = end

    while curr is not None:
        print(curr, end=" -> ")
        curr = parents[curr]
    print("*")
