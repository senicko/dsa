"""
Korzystamy ze wzoru log(a * b) = log(a) + log(b)
"""
from queue import PriorityQueue
from math import inf, log


def dijkstra(graph, s):
    n = len(graph)

    parents = [None] * n
    visited = [False] * n
    dist = [inf] * n
    dist[s] = 1

    queue = PriorityQueue()
    queue.put((dist[s], s))

    while not queue.empty():
        _, v = queue.get()

        if visited[v]:
            continue

        visited[v] = True

        for u, w in graph[v]:
            # We use the fact that log(ab) = log(a) + log(b)
            # so adding logarithms of weights together, finds
            # the smallest product of weights (log is ascending).
            if dist[u] > dist[v] + log(w):
                dist[u] = dist[v] + log(w)
                parents[u] = v

    return dist, parents


if __name__ == "__main__":
    graph = []
