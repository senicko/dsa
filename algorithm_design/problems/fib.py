def fib_top_down(n, cache):
    if n == 1:
        return 0

    if n == 2:
        return 1

    if cache[n] > 0:
        return cache[n]

    res = fib_top_down(n - 1, cache) + fib_top_down(n - 2, cache)
    cache[n] = res

    return res


def fib_bottom_up(n):
    dp = [-1] * (max(n + 1, 3))

    dp[1] = 0
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    n = 4
    result = fib_top_down(n, [-1] * (n + 1))

    print(result)

    assert result == fib_bottom_up(n)
