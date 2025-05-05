"""
Straight Facts:

In the main loop (*)

1) dist[u][v], dist[u][k] and dist[k][u] are
lengths of paths between nodes, which intermediate
nodes are from set V = { 1, ..., k - 1 }.

2) We can check if dist[u][v] > dist[u][k] + dist[k][v]
and if so, replace the shortest path between u and v
with one that contains k as intermediate node.
"""

from math import inf


def floyd_warshall(graph):
    n = len(graph)

    dist = [[inf] * n for _ in range(n)]

    for u in range(n):
        dist[u][u] = 0

        for v, w in graph[u]:
            dist[u][v] = w

    for k in range(n):
        for u in range(n):
            for v in range(n):
                # (*)
                if dist[u][v] > dist[u][k] + dist[k][v]:
                    dist[u][v] = dist[u][k] + dist[k][v]

    return dist
