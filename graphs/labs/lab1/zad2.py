# Policzyć liczbę spójnych składowych.


def count_components(graph):
    n = len(graph)
    visited = [False] * n

    def dfs_visit(v):
        visited[v] = True

        for u in graph[v]:
            if not visited[u]:
                dfs_visit(u)

    counter = 0

    for v in range(n):
        if not visited[v]:
            # Every time we backtrack to this loop, we have discovered
            # a new component.
            counter += 1
            dfs_visit(v)

    return counter


if __name__ == "__main__":
    graph = [
        [1, 4],  # 0
        [0, 2],  # 1
        [1, 3],  # 2
        [2],  # 3
        [0, 2]  # 4
    ]

    print(count_components(graph))
