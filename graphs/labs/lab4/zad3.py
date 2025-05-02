"""
Floyd Warshal, Dijkstra

Znajdywanie cyklu o najmniejszej wadze.

Ustawiamy odległości wierzchołków samych do siebie na inf.
Kiedy u == v, będziemy porównywać inf ze ścieżką idącą z u do u przez k, czyli cyklem.
"""

from math import inf


def find_min_cycle(graph):
    n = len(graph)

    dist = [[inf] * n for _ in range(n)]

    for u in range(n):
        # We can set distance to a node itself
        # to infinity so that we'll count the
        # shortest cycle.
        dist[u][u] = inf

        for v, w in graph[u]:
            dist[u][v] = w

    for k in range(n):
        for u in range(n):
            for v in range(n):
                # If u == v, in standard Floyd-Warshall nothing would happen,
                # but if dist[u][v] = inf, we'll replace the distance
                # with the shortest cycle.

                if dist[u][v] > dist[u][k] + dist[k][v]:
                    dist[u][v] = dist[u][k] + dist[k][v]

    min_cycle = inf

    for u in range(n):
        min_cycle = min(dist[u][u], min_cycle)

    return min_cycle


if __name__ == "__main__":
    graph = [
        [(1, 2)],  # Node 0 → Node 1 (weight 2)
        [(2, 3)],  # Node 1 → Node 2 (weight 3)
        [(3, 4)],  # Node 2 → Node 3 (weight 4)
        [(1, 1), (4, 5)],  # Node 3 → Node 1 (weight 1), Node 4 (weight 5)
        []  # Node 4 → No outgoing edges
    ]

    print(find_min_cycle(graph))
