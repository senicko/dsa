# Sprawdzenie, czy graf jest dwudzielny.

from collections import deque


def is_bipartite_list(graph, s):
    n = len(graph)
    queue = deque()

    # State
    # We will color nodes in 1 and -1
    colors = [None] * n

    # Init start vertex
    # Color starting node
    colors[s] = 1
    queue.appendleft(s)

    while queue:
        v = queue.pop()

        for u in graph[v]:
            if colors[u] is None:
                colors[u] = colors[v] * -1
                queue.appendleft(u)
            # Two connected nodes have the same color.
            # The graph is not bipartite.
            elif colors[u] == colors[v]:
                return False

            # If we don't meet any of the above conditions everything is fine.
            # It means that node u was already visited, but it has the color we
            # wanted to assign.

    return True


# The same thing but with adjacency matrix representation.
def is_bipartite_matrix(graph, s):
    n = len(graph)
    queue = deque()

    # State
    colors = [None] * n

    # Init start vertex
    colors[s] = 1
    queue.appendleft(s)

    while queue:
        v = queue.pop()

        for u in range(n):
            if graph[v][u] == 0:
                continue

            if colors[u] is None:
                colors[u] = colors[v] * -1
                queue.appendleft(u)
            elif colors[v] == colors[u]:
                return False

    return True


if __name__ == "__main__":
    graph_list = [
        [1, 4],  # 0
        [0, 2],  # 1
        [1, 3],  # 2
        [2],  # 3
        [0, 2]  # 4
    ]

    graph_matrix = [
        # 0  1  2  3  4
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0],
    ]

    list_result = is_bipartite_list(graph_list, 0)
    matrix_result = is_bipartite_matrix(graph_matrix, 0)

    assert list_result == matrix_result
    print(list_result)
