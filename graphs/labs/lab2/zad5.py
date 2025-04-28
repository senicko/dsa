def eulerian_cycle_matrix(G):
    n = len(G)
    next_edge_to = [0] * n
    cycle = []

    # Verify that eulerian cycle exists.
    for i in range(n):
        if sum(G[i]) % 2 != 0:
            return None

    def dfs_visit(u):
        nonlocal next_edge_to, G

        # Process outgoing edges.
        while next_edge_to[u] < n:
            v = next_edge_to[u]
            next_edge_to[u] += 1

            if G[u][v] == 1:
                G[u][v], G[v][u] = 0, 0
                dfs_visit(v)

        # After processing a vertex, add it to
        # the final cycle.
        cycle.append(u)

    # Start at a random node.
    # We can do that as we are searching
    # for an eulerian cycle, not an eulerian path,
    # in which case we need to find the start vertex that
    # has uneven number of edges.

    dfs_visit(0)
    return cycle


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 1, 0, 1],
        [0, 0, 1, 1, 0]
    ]

    print(eulerian_cycle_matrix(graph))
