from math import inf

def cut_tree(T):
    n = len(T)
    dp = [-inf] * n

    for i in range(n):
        dp[i] = max(
            dp[i - 2] + T[i] if i - 2 >= 0 else T[i],
            dp[i - 1] if i - 1 >= 0 else -inf
        )

    return dp[n - 1]


if __name__ == "__main__":
    print(cut_tree([2, 8, 3, 6]))
