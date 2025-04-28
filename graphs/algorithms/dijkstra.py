from math import inf
from queue import PriorityQueue


def dijkstra(G, s):
    n = len(G)
    parents = [None] * n
    visited = [False] * n

    dist = [inf] * n
    dist[s] = 0

    queue = PriorityQueue()
    queue.put((dist[s], s))

    while not queue.empty():
        v_dist, v = queue.get()

        # If we have already found a shorter path
        # to v, continue.
        if visited[v]:
            continue

        visited[v] = True

        for u, w in G[v]:
            if not visited[u] and dist[u] > dist[v] + w:
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
