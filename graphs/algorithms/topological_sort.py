def topological_sort(graph):
    n = len(graph)
    result = []
    visited = [False] * n

    def dfs_visit(v):
        nonlocal result
        visited[v] = True

        for u in graph[v]:
            if not visited[u]:
                dfs_visit(u)

        # Regular DFS. We are just adding
        # nodes to the result array.

        result.append(v)

    for v in range(n):
        if not visited[v]:
            dfs_visit(v)

    # At the end we have to reverse the result
    # array as in line 17, we actually want
    # to append to the beginning of the list.

    return reversed(result)


if __name__ == "__main__":
    names = {
        0: "undershorts",
        1: "pants",
        2: "belt",
        3: "shirt",
        4: "tie",
        5: "jacket",
        6: "shoes",
        7: "socks",
        8: "watch"
    }

    graph = [
        [1, 6],
        [2, 6],
        [5],
        [2, 4],
        [5],
        [],
        [],
        [6],
        []
    ]

    sorted_events = topological_sort(graph)
    print([names[e] for e in sorted_events])
