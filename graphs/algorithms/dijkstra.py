from math import inf
from queue import PriorityQueue


def dijkstra(G, s):
    n = len(G)

    dist = [inf] * n
    visited = [False] * n
    parents = [None] * n
    dist[s] = 0

    queue = PriorityQueue()
    queue.put((dist[s], s))

    while not queue.empty():
        _, v = queue.get()

        # Skip already visited vertices.
        # It is possible that some vertices
        # will be put to the queue multiple times.

        if visited[v]:
            continue

        # At this point we know that there is no better path to v.
        # If there was a better path, there would be a vertex u
        # with dist[u] < dist[v]. Because of that, we can mark v
        # as visited.

        visited[v] = True

        for u, w in G[v]:
            # Inlined relax. Note that we don't have
            # to check if u was visited, because
            # it's distance is for sure less.

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
