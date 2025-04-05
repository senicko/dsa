from collections import deque


def has_cycle(graph):
    n = len(graph)

    visited = [False for _ in range(n)]
    visited[0] = True

    queue = deque()
    queue.appendleft(0)

    while queue:
        v = queue.pop()

        for u in graph[v]:
            # If at this point we tried to go to a node
            # which was already visited, there must be a cycle.
            if visited[u]:
                return True

            visited[u] = True
            queue.appendleft(u)

    return False


if __name__ == "__main__":
    graph = [
        [1, 4],
        [2],
        [3],
        [],
        [2]
    ]

    print(has_cycle(graph))
