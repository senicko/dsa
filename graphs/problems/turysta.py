from egzP1btesty import runtests
from queue import PriorityQueue
from math import inf


def get_adj(G):
    n = max(map(lambda x: max(x[0], x[1]), G)) + 1

    adj = [[] for _ in range(n)]

    for u, v, w in G:
        adj[u].append((v, w))
        adj[v].append((u, w))

    return adj, n


def turysta(G, D, L):
    adj, n = get_adj(G)

    dist = [[inf] * 5 for _ in range(n)]
    queue = PriorityQueue()

    dist[D] = [0] * 5
    queue.put((dist[D][0], D, 0))

    while not queue.empty():
        d, u, visits = queue.get()

        # If we have reached the airport,
        # we have found the shortest path
        # through 3 attractions.
        if u == L:
            return d

        # If we have found a shorter path
        # to an attraction at u, continue.
        if d > dist[u][visits]:
            continue

        for v, w in adj[u]:
            # If we have visited 3 attractions
            # already, force choosing the airport.
            if visits == 3 and v != L or visits < 3 and v == L:
                continue

            alt = d + w

            if dist[v][visits + 1] > alt:
                dist[v][visits + 1] = alt
                queue.put((alt, v, visits + 1))


runtests(turysta)
