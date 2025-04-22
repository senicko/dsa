from math import inf


def dfs_list(graph):
    n = len(graph)

    time = 0
    visited = [False] * n
    parent = [None] * n
    discovery = [inf] * n
    processed = [inf] * n

    def dfs_visit(v):
        nonlocal time

        # Increment time at visit
        time += 1
        discovery[v] = time
        visited[v] = True

        for u in graph[v]:
            if not visited[u]:
                parent[u] = v
                dfs_visit(u)

        # Increment time at backtrack
        time += 1
        processed[v] = time

    for v in range(n):
        if not visited[v]:
            dfs_visit(v)

    return visited, parent, discovery, processed


def dfs_matrix(graph):
    n = len(graph)

    time = 0
    visited = [False] * n
    parent = [None] * n
    discovery = [inf] * n
    processed = [inf] * n

    def dfs_visit(v):
        nonlocal time

        # Increment time at visit
        time += 1
        visited[v] = True
        discovery[v] = time

        for u in range(n):
            if graph[v][u] == 1 and not visited[u]:
                parent[u] = v
                dfs_visit(u)

        # Increment time at backtrack
        time += 1
        processed[v] = time

    for v in range(n):
        if not visited[v]:
            dfs_visit(v)

    return visited, parent, discovery, processed


if __name__ == "__main__":
    graph_list = [
        [1, 4],
        [2],
        [3],
        [],
        [2]
    ]

    graph_matrix = [
        [0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]

    result_list = dfs_list(graph_list)
    result_matrix = dfs_matrix(graph_matrix)
    assert result_list == result_matrix
    print(result_list)
