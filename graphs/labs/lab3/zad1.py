from queue import PriorityQueue
from math import inf


def dijkstra(graph, s):
    n = len(graph)
    visited = [False] * n
    parents = [None] * n

    dist = [inf] * n
    dist[s] = 0

    queue = PriorityQueue()
    queue.put((0, s))

    while not queue.empty():
        d, v = queue.get()

        if visited[v]:
            continue

        visited[v] = True

        for u, w in graph[v]:
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                parents[u] = v
                queue.put((dist[u], u))

    return dist, parents


if __name__ == "__main__":
    graph = [
        [(1, 10), (5, 9999)],
        [(0, 10), (2, 10)],
        [(1, 10), (3, 10)],
        [(2, 10), (4, 10)],
        [(3, 10), (5, 9999)],
        [(0, 9999), (4, 9999)]
    ]

    print(dijkstra(graph, 0))
