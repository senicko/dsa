from queue import PriorityQueue
from math import inf


def lowest_fuel_price(graph, s, prices, D):
    n = len(graph)

    visited = [[False for _ in range(D + 1)] for v in range(n)]

    costs = [[inf] * (D + 1) for _ in range(n)]
    costs[s] = [0] * (D + 1)

    queue = PriorityQueue()
    queue.put((0, s, D))

    while not queue.empty():
        _, v, fuel = queue.get()

        if visited[v][fuel]:
            continue

        visited[v][fuel] = True

        for u, w in graph[v]:
            # Dolewamy od 0 do x litrów paliwa, tak
            # żeby fuel + x = D.

            for fill in range(D - fuel + 1):
                new_fuel = fuel + fill

                # Sprawdzamy, czy na pewno mamy wystarczająco
                # paliwa, żeby dojechać do kolejnego miasta.
                if new_fuel < w:
                    continue

                price = fill * prices[v]
                cost = costs[v][fuel] + price

                # Odejmujemy od nowego poziomu paliwa
                # ilość paliwa, która zostanie zużyta
                # na dojechanie do kolejnego miasta.
                new_fuel -= w

                # Relax
                if costs[u][new_fuel] > cost:
                    costs[u][new_fuel] = cost
                    queue.put((cost, u, new_fuel))

    return costs


if __name__ == "__main__":
    graph = [
        [(1, 4), (2, 2)],  # Miasto 0
        [(0, 4), (2, 1), (3, 5)],  # Miasto 1
        [(0, 2), (1, 1), (3, 8), (4, 10)],  # Miasto 2
        [(1, 5), (2, 8), (4, 2)],  # Miasto 3
        [(2, 10), (3, 2)]  # Miasto 4
    ]

    prices = [5, 2, 4, 7, 3]
    D = 10

    print(lowest_fuel_price(graph, 0, prices, D))
