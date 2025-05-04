from queue import PriorityQueue
from math import inf


def get_adj_list(edges):
    n = max(map(lambda x: max(x[0], x[1]), edges)) + 1
    graph = [[] for _ in range(n)]

    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph, n


def warrior(G, s, t):
    adj, n = get_adj_list(G)

    dist = [[inf] * 17 for _ in range(n)]
    dist[0] = [0] * 17

    queue = PriorityQueue()
    queue.put((0, s, 16))

    while not queue.empty():
        d, u, stamina = queue.get()

        if d > dist[u][stamina]:
            continue

        for v, w in adj[u]:
            real_w = w
            real_stamina = stamina

            if real_w > real_stamina:
                real_w += 8
                real_stamina = 16

            real_stamina -= w

            if dist[v][real_stamina] > d + real_w:
                dist[v][real_stamina] = d + real_w
                queue.put((dist[v][real_stamina], v, real_stamina))

    return min(dist[t])
