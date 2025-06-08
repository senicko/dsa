type Items = list[tuple[int, int, int]]

def knapsack2d(items: Items, max_height, max_weight):
    n = len(items)
    dp = [[[0] * (max_height + 1) for _ in range(max_weight + 1)] for _ in range(n + 1)]

    for w in range(max_weight + 1):
        for h in range(max_height + 1):
            for i in range(n):
                value, weight, height = items[i]
                dp[i][w][h] = dp[i-1][w][h]

                if weight <= w and height <= h:
                    dp[i][w][h] = max(dp[i][w][h], dp[i - 1][w - weight][h - height] + value)

    return dp[n - 1][max_weight][max_height]
