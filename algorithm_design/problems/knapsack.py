type Items = list[tuple[int, int]]
type Cache = list[list[int]]


def knapsack_top_down_aux(items: Items, i: int, capacity: int, cache: Cache):
    # What's the maximum value in knapsack, if we pack nonexistent item
    # at index 1?

    if i == len(items):
        return 0

    # Have we computed the solution to this subproblem before?

    if cache[i][capacity] > -1:
        return cache[i][capacity]

    result = knapsack_top_down_aux(items, i + 1, capacity, cache)
    value, size = items[i]

    if size <= capacity:
        result = max(result, knapsack_top_down_aux(items, i + 1, capacity - size, cache) + value)

    # Cache the result for this subproblem.

    cache[i][capacity] = result

    return result


def knapsack_top_down(items: Items, capacity: int):
    n = len(items)
    cache = [[-1] * (capacity + 1) for _ in range(n)]
    return knapsack_top_down_aux(items, 0, capacity, cache)


def knapsack_bottom_up(items: Items, capacity: int):
    n = len(items)

    # Translate recursive approach directly.
    # Create a 2d array that will store results for our subproblems.

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        value, size = items[i]

        for s in range(size, capacity + 1):
            dp[i][s] = max(dp[i + 1][s], dp[i + 1][s - size] + value)

    return dp[0][capacity]


def knapsack_bottom_up_optimised(items: Items, capacity: int):
    # We can notice, that single dimension dp array,
    # just for capacities, is enough.

    dp = [0] * (capacity + 1)

    for value, size in items:

        # By computing subproblems in order of capacity -> size,
        # we know that referring to dp[s - size] doesn't  contain
        # result which considered current item.

        for s in range(capacity, size - 1, -1):
            dp[s] = max(dp[s], dp[s - size] + value)

    return dp[capacity]


if __name__ == "__main__":
    items = [(60, 10), (100, 20), (120, 30)]  # (value, size)
    capacity = 50
    expected = 220

    assert knapsack_top_down(items, capacity) == knapsack_bottom_up(items, capacity) \
           == knapsack_bottom_up_optimised(items, capacity) == expected

    print(f"ok, expected: {expected}")
