from math import inf


UP = 0
DOWN = 1
ARBITRARY = 2


def in_bounds(i, j, n):
    return 0 <= i < n and 0 <= j < n


def maze_aux(L, i, j, next_move, cache):
    n = len(L)

    if not in_bounds(i, j, n) or L[i][j] == "#":
        return -inf

    if i == 0 and j == 0:
        return 0

    if cache[i][j][next_move]:
        return cache[i][j][next_move]

    cache[i][j][next_move] = max(
        maze_aux(L, i - 1, j, DOWN, cache) if next_move != UP else -inf,
        maze_aux(L, i + 1, j, UP, cache) if next_move != DOWN else -inf,
        maze_aux(L, i, j - 1, ARBITRARY, cache)
    ) + 1

    return cache[i][j][next_move]


def maze(L):
    n = len(L)
    cache = [[[None] * 3 for _ in range(n)] for _ in range(n)]
    return max(maze_aux(L, n - 1, n - 1, ARBITRARY, cache), -1)
