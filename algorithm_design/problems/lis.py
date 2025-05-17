def lis_top_down_aux(a, i, cache):
    if cache[i] > 0:
        return cache[i]

    res = 1

    for k in range(i):
        # If a[k] < a[i], so if lis ending at k can
        # be extended by a[i], take max.
        if a[k] < a[i]:
            res = max(res, lis_top_down_aux(a, k, cache) + 1)

    cache[i] = res
    return res


def lis_top_down(a):
    n = len(a)
    return lis_top_down_aux(a, n - 1, [-1] * n)


def lis_bottom_up(a):
    n = len(a)
    dp = [1] * n
    parents = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parents[i] = j

    return dp[n - 1], parents


def print_lis(a, p, i):
    if p[i] != -1:
        print_lis(a, p, p[i])

    print(a[i])


if __name__ == "__main__":
    a = [10, 22, 9, 33, 21, 50, 41, 60]
    n = len(a)
    result, parents = lis_bottom_up(a)
    assert result == lis_top_down(a)
    print_lis(a, parents, n - 1)
