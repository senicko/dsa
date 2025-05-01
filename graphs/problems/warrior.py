from collections import deque
from math import inf


def process_graph(G):
    n = -inf

    for u, v, w in G:
        n = max(n, u, v)

    graph = [[] for _ in range(n + 1)]

    for u, v, w in G:
        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph


def warrior(graph, s, t):
    graph = process_graph(graph)
    n = len(graph)

    dist = [[inf] * 17 for _ in range(n)]

    queue = deque()
    queue.append((s, 0, 16, 0))  # (v, steps, stamina, journey)

    while queue:
        u, steps, stamina, journey = queue.popleft()

        if dist[u][stamina] < journey:
            continue

        if steps != 0:
            queue.append((u, steps - 1, stamina, journey))
            continue

        for v, w in graph[u]:
            real_w = w
            real_stamina = stamina

            if w > stamina:
                real_w += 8
                real_stamina = 16

            real_stamina -= w
            new_journey = journey + real_w

            if new_journey < dist[v][real_stamina]:
                dist[v][real_stamina] = new_journey
                queue.append((v, real_w - 1, real_stamina, new_journey))

    return min(dist[t])
