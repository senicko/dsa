"""
Pomysł:
    Dla każdego wierzchołka uruchamiamy DFS. Odwiedzamy n wierzchołków.
    Przy n-tym wierzchołku sprawdzamy, czy istnieje połączenie pomiędzy nim a wierzchołkiem
    startowym. Jak tak to znaleźliśmy cykl, jak nie to oznaczamy wierzchołek startowy jako odwiedzony
    i idziemy do następnego.

    (*) Musimy zadbać o to, żeby wszystkie wierzchołki, które oznaczyliśmy jako odwiedzone
        podczas sprawdzania cyklu dla jakiegoś wierzchołka, z powrotem stały się nieodwiedzone.
"""


def has_n_cycle(graph, n):
    n = len(graph)
    visited = [False] * n

    def dfs_visit(v, start, left):
        visited[v] = True

        # If we've used enough vertices to
        # create a cycle.
        if left == 0:
            # Check if there is a connection between start and v
            if graph[v][start] == 1 and graph[start][v] == 1:
                print("B")
                return True
            else:
                # (*)
                visited[v] = False
                return False

        # Continue as in regular DFS
        for u in range(n):
            if graph[v][u] == 0:
                continue

            if not visited[u]:
                if dfs_visit(u, start, left - 1):
                    return True

        # (*)
        visited[v] = False

    for v in range(n):
        if not visited[v]:
            if dfs_visit(v, v, n - 1):
                print("C")
                return True
            visited[v] = True

    return False


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0]
    ]

    print(has_n_cycle(graph, 4))
