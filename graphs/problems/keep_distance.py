from zad1testy import runtests
from collections import deque
from math import inf


def floyd_warshall(graph):
    n = len(graph)
    dist = [[inf] * n for _ in range(n)]

    for u in range(n):
        dist[u][u] = 0

        for v in range(n):
            if graph[u][v] == 0:
                continue

            dist[u][v] = graph[u][v]

    for k in range(n):
        for u in range(n):
            for v in range(n):
                alt = dist[u][k] + dist[k][v]
                if dist[u][v] > alt:
                    dist[u][v] = alt

    return dist


def keep_distance(M, x, y, d):
    n = len(M)
    dist = floyd_warshall(M)

    if dist[x][y] < d:
        return None

    visited = [[False] * n for _ in range(n)]
    queue = deque()
    queue.append((x, y, [(x, y)]))
    visited[x][y] = True

    while queue:
        u, v, path = queue.popleft()

        if (u, v) == (y, x):
            return path

        # Get all possible next moves (including "wait")
        next_u_list = [u] + [i for i in range(n) if M[u][i] > 0]
        next_v_list = [v] + [j for j in range(n) if M[v][j] > 0]

        for next_u in next_u_list:
            for next_v in next_v_list:
                # Nie mogą się minąć na tej samej krawędzi w przeciwnych kierunkach
                if next_u == v and next_v == u:
                    continue

                # Muszą być w odpowiedniej odległości
                if dist[next_u][next_v] < d:
                    continue

                if not visited[next_u][next_v]:
                    visited[next_u][next_v] = True
                    queue.append((next_u, next_v, path + [(next_u, next_v)]))

    return None


runtests(keep_distance)
