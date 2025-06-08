from math import inf


def matrix_chain_multiplication(p):
    # n is the number of dimensions given in p,
    # not the number of matrices (!) (there are n - 1 of them).
    n = len(p)

    # Because A(i) is of dimensions p[i - 1] ⨯ p[i],
    # matrices can be thought of as indexed from 1 up to n - 1.

    dp = [[inf] * n for _ in range(n)]
    cuts = [[-1] * n for _ in range(n)]

    # Parenthesization of a single matrix costs 0.
    for i in range(1, n):
        dp[i][i] = 0

    # For every possible chain length, ranging from 2 up to n - 1.
    for length in range(2, n):

        # Pick the first matrix in the chain.
        # Choices range from 1 up to n - length.
        for i in range(1, n - length + 1):

            # We add length to i, but then also subtract 1,
            # as A(i) belongs to the chain.
            j = i + length - 1

            # Now pick the "cut / parenthesization" point,
            # ranging from i up to j - 1.
            for k in range(i, j):
                alt = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]

                if dp[i][j] > alt:
                    dp[i][j] = alt
                    cuts[i][j] = k

    return dp[1][n - 1], cuts


if __name__ == "__main__":
    p = [30, 35, 15, 5, 10, 20, 25]
    cost, cuts = matrix_chain_multiplication(p)
    print(cost)
