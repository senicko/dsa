def lcs_top_down_aux(x, y, xi, yi, cache):
    if xi == -1 or yi == -1:
        return 0

    if cache[xi][yi] > -1:
        return cache[xi][yi]

    if x[xi] == y[yi]:
        cache[xi][yi] = lcs_top_down_aux(x, y, xi - 1, yi - 1, cache) + 1
    else:
        cache[xi][yi] = max(lcs_top_down_aux(x, y, xi - 1, yi, cache), lcs_top_down_aux(x, y, xi, yi - 1, cache))

    return cache[xi][yi]


def lcs_top_down(x, y):
    xn = len(x)
    yn = len(y)
    cache = [[-1] * yn for _ in range(xn)]

    return lcs_top_down_aux(x, y, xn - 1, yn - 1, cache)


def lcs_bottom_up(x, y):
    xn = len(x) + 1
    yn = len(y) + 1

    # Initialize dp state.

    dp = [[-1] * yn for _ in range(xn)]
    s = [[""] * yn for _ in range(xn)]

    # Fill edges of dp array with 0.

    for i in range(xn):
        dp[i][yn - 1] = 0

    for i in range(yn):
        dp[xn - 1][i] = 0

    # Solve subproblems.

    for xi in range(xn - 2, -1, -1):
        for yi in range(yn - 2, -1, -1):
            # If two characters are the same,
            # take the previous solution and add one.
            if x[xi] == y[yi]:
                dp[xi][yi] = dp[xi + 1][yi + 1] + 1
                s[xi][yi] = "append"
            else:
                # If two characters aren't the same
                # override current solution with the current best,
                # and proceed to the next character.
                if dp[xi + 1][yi] > dp[xi][yi + 1]:
                    dp[xi][yi] = dp[xi + 1][yi]
                    s[xi][yi] = "down"
                else:
                    dp[xi][yi] = dp[xi][yi + 1]
                    s[xi][yi] = "right"

    return dp[0][0], s


def print_lcs(x, y, s, i, j):
    if i == len(x) or j == len(y):
        print('\n')
        return

    if s[i][j] == "append":
        print(x[i], end="")
        print_lcs(x, y, s, i + 1, j + 1)
    elif s[i][j] == "down":
        print_lcs(x, y, s, i + 1, j)
    else:
        print_lcs(x, y, s, i, j + 1)


if __name__ == "__main__":
    x = "ACDBEAG"
    y = "ABCDEG"

    length, solution = lcs_bottom_up(x, y)

    print(length)
    print_lcs(x, y, solution, 0, 0)
