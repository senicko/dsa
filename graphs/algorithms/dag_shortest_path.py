"""
Cool application: PERT chart
"""

from math import inf


def topological_sort(G):
    n = len(G)
    visited = [False] * n
    order = []

    def dfs_visit(v):
        visited[v] = True

        for u, _ in G[v]:
            if not visited[u]:
                dfs_visit(u)

        order.append(v)

    for v in range(n):
        if not visited[v]:
            dfs_visit(v)

    order.reverse()
    return order


def dag_shortest_path(G, s):
    n = len(G)

    distances = [inf] * n
    distances[s] = 0
    parents = [None] * n

    order = topological_sort(G)

    def relax(v, u, w):
        if distances[u] > distances[v] + w:
            distances[u] = distances[v] + w
            parents[u] = v

    # We're making use of the fact that our graph is
    # a DAG by relaxing edges in topological order.

    for v in order:
        for u, w in G[v]:
            relax(v, u, w)

    return distances, parents


if __name__ == "__main__":
    graph = [
        [(1, 2), (2, 4), (3, 2)],
        [],
        [(3, 4)],
        []
    ]

    print(dag_shortest_path(graph, 0))
