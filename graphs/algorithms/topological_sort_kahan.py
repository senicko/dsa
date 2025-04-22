from collections import deque


def topological_sort_kahan(graph):
    n = len(graph)
    result = []

    # Count in-degree of every vertex
    # in the graph.

    in_deg = [0] * n

    for v in range(n):
        for u in graph[v]:
            in_deg[u] += 1

    # Add vertices with in-degree of 0
    # to a queue.

    queue = deque([v for v in range(n) if in_deg[v] == 0])

    while queue:
        v = queue.pop()
        result.append(v)

        # Update in-degree of v's neighbours
        # by decrementing them by one.

        for u in graph[v]:
            in_deg[u] -= 1

            # If u's in-degree reached 0,
            # add it to the queue.

            if in_deg[u] == 0:
                queue.appendleft(u)

    return result


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

    sorted_events = topological_sort_kahan(graph)
    print([names[e] for e in sorted_events])
