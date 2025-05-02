"""
Sortujemy krawedzie po wagach

potem przechodzimy liniowo. Jak jest krawedz miedzy nieodwiedzonymi wierzcholkami to ja odrzucamy
bo na pewno jej nie uzyjemy (bo musielibysmy odwiedzic wczesniej)

dystans dla parzystych i nieparzystych odwiedzen,
mnożenie wierzchołków
"""
from math import inf


def extract_edges(graph):
    n = len(graph)
    edges = []

    for u in range(n):
        for v, w in graph[u]:
            edges.append((u, v, w))

    return edges


def shortest_desc(graph, x, y):
    n = len(graph)

    visited = [False] * n
    visited[x] = True

    parents = [None] * n
    dist = [inf] * n

    edges = extract_edges(graph)
    edges.sort(key=lambda e: e[2], reverse=True)

    for u, v, w in edges:
        if not visited[u]:
            continue

        visited[v] = True

        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            parents[v] = u

    # Check if we have found any path.

    if dist[y] == inf:
        return None

    # Reconstruct the path.

    path = []
    v = y

    while v:
        path.append(v)
        v = parents[v]

    return dist[y], path


if __name__ == "__main__":
    graph = []
