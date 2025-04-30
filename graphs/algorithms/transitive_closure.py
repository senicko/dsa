def transitive_closure(graph):
    n = len(graph)

    result = [[0] * n for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if graph[u][v]:
                result[u][v] = 1

    for k in range(n):
        # k is the end vertex in set of intermediate vertices.
        # So At every iteration V = { 1, ..., k - 1 } is a set
        # of vertices that were examined to construct paths
        # between every two vertices.

        for u in range(n):
            for v in range(n):
                if u == v:
                    continue

                # Here, we check if it's possible to reach
                # v from u using k as an intermediate vertex.
                if result[u][k] == 1 and result[k][v] == 1:
                    result[u][v] = 1

    return result


if __name__ == "__main__":
    graph = [
        [0, 1, 0, 0, 1, 0],  # edges: 0-1, 0-4
        [1, 0, 1, 0, 1, 0],  # edges: 1-0, 1-2, 1-4
        [0, 1, 0, 1, 0, 0],  # edges: 2-1, 2-3
        [0, 0, 1, 0, 0, 1],  # edges: 3-2, 3-5
        [1, 1, 0, 0, 0, 0],  # edges: 4-0, 4-1
        [0, 0, 0, 1, 0, 0],  # edge: 5-3
    ]

    print(*transitive_closure(graph), sep="\n")
