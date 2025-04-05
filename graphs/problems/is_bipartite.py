from collections import deque


def is_bipartite(graph):
    n = len(graph)
    queue = deque()
    colors = [-1] * n

    for v in range(n):
        # If vertex was already visited.
        if colors[v] != -1:
            continue

        # Put starting vertex of the new component
        # to the queue.
        colors[v] = 0
        queue.appendleft(v)

        while queue:
            u = queue.pop()

            for w in graph[u]:
                # The vertex doesn't have a color yet.
                if colors[w] == -1:
                    colors[w] = 1 - colors[u]
                    queue.append(w)
                # Adjacent vertex has the same color,
                # so our graph is not bipartite.
                elif colors[w] == colors[u]:
                    return False

                # Adjacent vertex was already visited,
                # but it has different color, so it's fine.

    return True


if __name__ == "__main__":
    graph = [
        [1, 4],
        [0, 2],
        [1, 3],
        [2],
        [0, 2]
    ]

    print(is_bipartite(graph))
