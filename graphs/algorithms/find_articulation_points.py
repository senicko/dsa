from math import inf


def find_articulation_points(graph):
    n = len(graph)

    time = 0
    low = [inf] * n
    discovery = [inf] * n
    visited = [False] * n

    articulation_points = []

    def dfs_visit(u, parent=-1):
        nonlocal time

        time += 1
        visited[u] = True
        low[u] = discovery[u] = time
        children = 0

        for v in graph[u]:
            if not visited[v]:
                children += 1
                dfs_visit(v, u)
                low[u] = min(low[v], low[u])

                # Note the >= operator. When we are looking for
                # articulation points >= is sufficient, contrary to
                # finding bridges, when we have to check if
                # low[v] > discovery[u].
                if parent != -1 and low[v] >= discovery[u]:
                    articulation_points.append(u)
            elif v != parent:
                low[u] = min(low[u], discovery[v])

        return children

    for u in range(n):
        if not visited[u]:
            children = dfs_visit(u)

            if children >= 2:
                articulation_points.append(u)

    return articulation_points


if __name__ == "__main__":
    graph = [
        [1, 2],
        [0, 2, 3],
        [0, 1],
        [1, 4],
        [3]
    ]

    print(find_articulation_points(graph))
