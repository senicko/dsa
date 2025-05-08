from math import inf


def floyd_warshall(graph):
    n = len(graph)
    dist = [[inf] * n for _ in range(n)]

    for u in range(n):
        dist[u][u] = 0

        for v, w in graph[u]:
            dist[u][v] = w
            dist[v][u] = w

    for k in range(n):
        for u in range(n):
            for v in range(n):
                alt = dist[u][k] + dist[k][v]

                if dist[u][v] > alt:
                    dist[u][v] = alt

    return dist


def robot(G, P):
    dist = floyd_warshall(G)

    w = 0
    for p in range(len(P) - 1):
        w += dist[P[p]][P[p + 1]]

    return w
