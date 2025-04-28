"""
sortujemy topologicznie + relaksacja po kolei w kolejnosci posortowanych wierzcholkow, co gwarantuje
najkrotsza sciezke

jeżeli s nie jest pierwszym wierzcholkiem sortowaniu topologicznym to ignorujemy wierzchołki przed nim.
"""

from math import inf


def topological_sort(graph):
    n = len(graph)
    visited = [False] * n
    order = []

    def dfs_visit(v):
        for u, _ in graph[v]:
            if not visited[u]:
                visited[u] = True
                dfs_visit(u)
        order.append(v)

    for v in range(n):
        if not visited[v]:
            visited[v] = True
            dfs_visit(v)

    order.reverse()
    return order


def shortest_dag(graph, s):
    n = len(graph)
    order = topological_sort(graph)
    parents = [None] * n
    dist = [inf] * n
    dist[s] = 0

    def relax(u, v, w):
        if dist[u] > dist[v] + w:
            dist[u] = dist[v] + w
            parents[u] = v

    for u in order:
        for v, w in graph[u]:
            relax(u, v, w)

    return dist, parents
