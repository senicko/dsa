"""
Obliczamy funkcję f(i, j), która mówi jaki jest najmniejszy koszt połączenia wejść
na przedziale [i, j + 1]. W każdym takim przedziale, szukamy k-tego wejścia w przedziale,
które połączymy z i-tym wejściem, i bierzemy koszt tego połączenia. Następnie wykorzystując
funkcję f, dodajemy od tego koszt wnętrza przedziału [i + 1 : k] oraz koszt pozostałego przedziału [k + 1 : j + 1].

f(i, j) = min for k in range(i + 1, j + 1): {
    1 + abs(T[i] - T[k]) +
    + f(i + 1, k - 1) +
    + f(k + 1, j) +
}
"""


from math import inf


def wired(T):
    n = len(T)
    dp = [[inf] * n for _ in range(n)]

    for l in range(2, n + 1, 2):
        for i in range(0, n - l + 1):
            j = i + l - 1

            for k in range(i + 1, j + 1, 2):
                dp[i][j] = min(
                    dp[i][j],
                    1 + abs(T[i] - T[k]) + \
                        # Zauważmy, że w momencie kiedy przedziały nie istnieją,
                        # dodajemy 0, żeby uniknąć wyjścia indeksami poza tablicę.
                        (dp[i + 1][k - 1] if i + 1 < k - 1 else 0) + \
                        (dp[k + 1][j] if k + 1 < j else 0)
                )

    return dp[0][n - 1]
