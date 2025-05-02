"""
Sorting         O(ElogE) <= O(ElogV^2) = O(ElogV)
Building MSTs   O(VElog*E) ~ O(VE)
Total:          O(ElogV + VE) = O(E(logV + V)) = O(EV)
"""

from math import inf, isinf


class Set:
    def __init__(self, v):
        self.v = v
        self.parent = self
        self.rank = 0


def find(x):
    if x is not x.parent:
        # Using "Path Compression" heuristic.
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    # Using "Rank" heuristic.
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y

        if x.rank == y.rank:
            y.rank += 1


# O(Elog*E) ~ O(E), because of "Path Compression" and "Rank" heuristics.
def kruskal(edges, n, i, j):
    sets = [Set(v) for v in range(n)]

    weight = 0
    mst = 0

    for e in range(i, j):
        u, v, w = edges[e]
        u = sets[u]
        v = sets[v]

        if find(u) != find(v):
            union(u, v)
            weight += w
            mst += 1

    return mst == n - 1, weight


def beautree(graph):
    n = len(graph)
    print(n)
    edges = []

    for u in range(n):
        for v, w in graph[u]:
            if v > u:
                edges.append((u, v, w))

    # Sorting takes O(ElogE)
    edges.sort(key=lambda x: x[2])

    m = len(edges)
    min_weight = inf

    # Here, we estimate the number of iterations by O(E)
    for i in range(m - n + 1):
        j = i + n - 1
        is_mst, weight = kruskal(edges, n, i, j)

        if is_mst:
            min_weight = min(min_weight, weight)

    return min_weight if not isinf(min_weight) else None
