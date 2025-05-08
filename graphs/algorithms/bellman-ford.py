from math import inf


def bellman_ford(G, s):
    n = len(G)

    dist = [inf] * n
    parent = [None] * n
    dist[s] = 0

    # Examine all of |E| edges |V| - 1 times.
    for _ in range(n - 1):
        for u in range(n):
            for v, w in G[u]:
                # Relax.
                alt = dist[u] + w

                if dist[v] > alt:
                    dist[v] = alt
                    parent[v] = u

    # Examine all edges.
    # Note that dist[v] <= dist[u] + w(u, v) (For All u that have an edge to v)
    # So if this condition is met everything is fine.
    for u in range(n):
        for v, w in G[u]:
            if dist[v] > dist[u] + w:
                return False

    return True
