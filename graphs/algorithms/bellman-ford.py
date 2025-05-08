from math import inf


def bellman_ford(G, s):
    n = len(G)

    dist = [inf] * n
    parent = [None] * n
    dist[s] = 0

    # Examine all of |E| edges |V| - 1 times
    for _ in range(n - 1):
        for u in range(n):
            for v, w in G[u]:
                alt = dist[u] + w

                if dist[v] > alt:
                    dist[v] = alt
                    parent[v] = u

    # Return a boolean value indicating whether
    # there is a negative-weight cycle reachable from
    # source vertex.
    for u in range(n):
        for v, w in G[u]:
            if dist[v] > dist[u] + w:
                return False

    return True


if __name__ == "__main__":
    graph = [
        [(1, 2), (2, 4), (3, 2)],
        [],
        [(3, 4)],
        []
    ]

    print(bellman_ford(graph, 0))
