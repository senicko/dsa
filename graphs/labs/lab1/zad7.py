"""
Takie zadania raczej są pod programowanie dynamiczne.

W tym przypadku wiemy, że wagi pól są z zakresu {1, ..., 5} przez
co możemy efektywnie wykorzystać algorytm BFS do wyznaczenia optymalnej ścieżki
(symulując wagi krawędzi sztucznymi wierzchołkami).

Musimy sobie wyobrazić, że mamy taki graf siatkę, gdzie do danego pola
wchodzą krawędzie o jego wadze.
"""

from collections import deque

MOVES = [[1, 0], [0, 1]]


def in_bounds(y, x, n):
    return 0 <= y < n and 0 <= x < n


def kings_path(A):
    n = len(A)
    queue = deque()

    # State

    visited = [[False] * n] * n

    # Process first position

    visited[0][0] = True
    queue.appendleft((0, 0, A[0][0]))  # (y, x, cost)
    A[0][0] = 0

    while queue:
        y, x, cost = queue.pop()

        if A[y][x] > 0:
            A[y][x] -= 1
            queue.appendleft((y, x, cost))
            continue

        # We can stop if we've arrived at index (n-1, n-1).
        # Because we've used BFS for board traversal,
        # we know we have found the shortest path.

        if y == n - 1 and x == n - 1:
            return cost

        # If none of the above conditions were met,
        # continue regular DFS.

        for my, mx in MOVES:
            ny, nx = y + my, x + mx

            if in_bounds(ny, nx, n):
                visited[ny][nx] = True
                queue.appendleft((ny, nx, cost + A[ny][nx]))


if __name__ == "__main__":
    board = [
        [1, 4, 7, 1, 3],
        [5, 8, 2, 9, 6],
        [1, 3, 4, 7, 2],
        [6, 2, 5, 1, 8],
        [9, 4, 3, 6, 7],
    ]

    print(kings_path(board))
