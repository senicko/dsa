from math import inf


def bellman_ford(G, s):
    n = len(G)

    distances = [inf] * n
    parent = [None] * n
    distances[s] = 0

    def relax(v, u, w):
        if distances[u] > distances[v] + w:
            distances[u] = distances[v] + w
            parent[u] = v

    # Examine all of |E| edges |V| - 1 times,
    # resulting in O(V^2 + VE) complexity.

    for _ in range(n - 1):
        for v in G:
            for u, w in v:
                relax(v, u, w)

    # Return a boolean value indicating whether
    # there is a negative-weight cycle reachable from
    # source vertex.

    for v in G:
        for u, w in v:
            if distances[u] > distances[v] + w:
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
