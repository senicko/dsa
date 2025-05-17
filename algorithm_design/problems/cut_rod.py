"""
The Rod Cutting Problem

Given a rod of length n inches and a table of prices p(i) for i = 1, ..., n, determine
the maximum revenue r(n) obtained by cutting up the rod and selling the pieces.

If the price p(n) for a rod of length n is large enough, an optimal solution might
require no cutting at all.

For detailed explanation see "Introduction To Algorithms" p. 365
"""

from math import inf


def naive_cut_rod(n, prices):
    if n == 0:
        return 0

    revenue = -inf

    # `i` represents the length of the segment we'll cut
    # from the left of the rod.
    for i in range(1, n + 1):
        revenue = max(revenue, prices[i] + naive_cut_rod(n - i, prices))

    return revenue


def top_down_memoization_cut_rod(n, prices, cache):
    if n == 0:
        return 0

    if cache[n] >= 0:
        return cache[n]

    r = -inf

    for i in range(1, n + 1):
        r = max(r, prices[i] + top_down_memoization_cut_rod(n - i, prices, cache))

    cache[n] = r
    return r


def bottom_up_cut_rod(n, prices):
    r = [-inf] * (n + 1)
    r[0] = 0

    cuts = [-1] * (n + 1)

    for j in range(1, n + 1):
        for i in range(1, j + 1):
            alt = prices[i] + r[j - i]

            if r[j] < alt:
                # Record that we've made
                # cut of length i.
                r[j] = alt
                cuts[j] = i

    return r[n], cuts


if __name__ == "__main__":
    N = 10
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    bottom_up, cuts = bottom_up_cut_rod(N, prices)

    assert \
        naive_cut_rod(N, prices) == \
        top_down_memoization_cut_rod(N, prices, [-inf] * (N + 1)) == \
        bottom_up

    while N > 0:
        print(cuts[N])
        N -= cuts[N]
