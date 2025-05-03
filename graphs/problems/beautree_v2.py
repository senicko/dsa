"""
Total: (V(V + E)) = O(V^2 + EV) ~ O(2EV) = O(VE)
"""

from collections import deque
from math import inf, isinf


def build_graph(edges, n, i, j):
    graph = [[] for _ in range(n)]
    total_w = 0

    for e in range(i, j):
        u, v, w = edges[e]
        total_w += w
        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph, total_w


def extract_edges(graph):
    n = len(graph)
    edges = []

    for u in range(n):
        for v, w in graph[u]:
            if u < v:
                edges.append((u, v, w))

    return edges, len(edges)


def is_connected(edges, n, i, j):
    graph, w = build_graph(edges, n, i, j)

    visited = [False] * n
    visited_count = 1
    queue = deque()

    visited[0] = True
    queue.append(0)

    while queue:
        u = queue.popleft()

        for v, _ in graph[u]:
            if not visited[v]:
                visited_count += 1
                visited[v] = True
                queue.append(v)

    return visited_count == n, w


def beautree(G):
    n = len(G)

    edges, m = extract_edges(G)
    edges.sort(key=lambda x: x[2])

    min_w = inf

    for i in range(m - n + 1):
        j = i + n - 1
        ok, w = is_connected(edges, n, i, j)

        if ok and w < min_w:
            min_w = w

    return min_w if not isinf(min_w) else None
