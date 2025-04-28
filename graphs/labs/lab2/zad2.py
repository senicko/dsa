from math import inf


def find_path(x, y, graph):
    n = len(graph)
    visited = [False] * n

    def dfs_visit(v, parent):
        # If we've found the destination node.
        if v == y:
            return True

        for u in range(n):
            # If edge to neighbour has lower
            # weight than parent edge.
            if graph[v][u] != 0 and graph[v][u] < parent:
                visited[u] = True
                if dfs_visit(u, graph[v][u]):
                    return True

        visited[v] = False
        return False

    visited[x] = True
    return dfs_visit(x, inf)


if __name__ == "__main__":
    graph = [
        [0, 2, 0, 0, 0],
        [2, 0, 3, 0, 0],
        [0, 3, 0, 4, 0],
        [0, 0, 4, 0, 5],
        [0, 0, 0, 5, 0]
    ]

    print(find_path(0, 3, graph))
