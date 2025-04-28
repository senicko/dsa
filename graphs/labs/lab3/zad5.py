from math import inf
from queue import PriorityQueue

ALICE = 0
BOB = 1


def alice_and_bob(graph, s):
    n = len(graph)

    parents = [[None, None] for _ in range(n)]
    visited = [[False, False] for _ in range(n)]

    dist = [[inf, inf] for _ in range(n)]
    dist[s][ALICE] = dist[s][BOB] = 0

    queue = PriorityQueue()
    queue.put((dist[s][ALICE], s, ALICE))
    queue.put((dist[s][BOB], s, BOB))

    while not queue.empty():
        _, v, prev_driver = queue.get()

        if visited[v][prev_driver]:
            continue

        visited[v][prev_driver] = True

        for u, w in graph[v]:
            next_driver = (prev_driver + 1) % 2

            if visited[u][next_driver]:
                continue

            w = 0 if next_driver == BOB else w
            cost = dist[v][prev_driver] + w

            if dist[u][next_driver] > cost:
                dist[u][next_driver] = cost
                parents[u][next_driver] = v
                queue.put((dist[u][next_driver], u, next_driver))

    return dist, parents


if __name__ == "__main__":
    drivers = ['alice', 'bob']

    for graph in [
        [
            [(1, 5), (3, 1)],
            [(2, 4)],
            [(3, 8)],
            [(4, 99), (0, 1)],
            [],
        ],
        [
            [(1, 5), (3, 99)],
            [(2, 4), (3, 1)],
            [(3, 8)],
            [(4, 99), (0, 1)],
            [],
        ]
    ]:
        dist, parents = alice_and_bob(graph, 0)

        curr = 4
        driver = ALICE if dist[curr][ALICE] < dist[curr][BOB] else BOB

        while curr is not None:
            print(f"{drivers[driver]} visits {curr}; distance by alice {dist[curr][driver]}")
            curr = parents[curr][driver]
            driver = (driver + 1) % 2

        print(min(dist[4]))
