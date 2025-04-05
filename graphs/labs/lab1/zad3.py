# Jakaś tam historyjka o sieci komórkowej ...
# Chcemy usuwać wierzchołki z grafu w taki sposób, aby do samego końca był spójny.


from collections import deque


def get_shutdown_order(network, s):
    n = len(network)
    queue = deque()

    visited = [False] * n

    # To keep the graph connected, we want to shut down
    # stations in order, from the furthest one to the nearest one.
    shutdown_order = []

    visited[s] = True
    shutdown_order.append(s)
    queue.appendleft(s)

    while queue:
        v = queue.pop()

        for u in network[v]:
            if not visited[u]:
                shutdown_order.append(s)
                visited[u] = True
                queue.appendleft(s)

    shutdown_order.reverse()
    return shutdown_order
