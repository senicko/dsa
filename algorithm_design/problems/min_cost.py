"""
Liczymy funkcję
    - T(i) = minimalny zapłacona kwota w momencie dojazdu do parkingu i.

Żeby to zadziałało, wstawiamy sztuczny parking w mieście B.
"""


from math import inf


def min_cost_aux(i, T, O, C, cache, cheated=False):
    if cache[i][cheated]:
        return cache[i][cheated]

    if O[i] <= T or not cheated and O[i] <= 2 * T:
        return 0

    n = len(O)
    cost = inf

    for j in range(n):
        dist = O[i] - O[j]

        if dist > 0 and \
            dist <= T or \
            not cheated and dist <= 2 * T:
            cheated = cheated or dist > T
            cost = min(cost, C[j] + min_cost_aux(j, T, O, C, cache, cheated))

    cache[i][cheated] = cost
    return cost


def min_cost_rec(O, C, T, L):
    O = O + [L]
    C = C + [0]

    n = len(O)
    cache = [[None, None] for _ in range(n)]

    return min_cost_aux(n - 1, T, O, C, cache)


def min_cost(O, C, T, L):
    O, C = zip(*sorted(list(zip(O + [L], C + [0]))))

    n = len(O)
    fair = [inf] * n
    unfair = [inf] * n

    for i in range(n):
        if O[i] <= T:
            fair[i] = unfair[i] = 0
            continue

        if O[i] <= 2 * T:
            unfair[i] = 0

        for k in range(i):
            dist = O[i] - O[k]

            if dist <= T:
                fair[i] = min(fair[i], C[k] + fair[k])
                unfair[i] = min(unfair[i], C[k] + unfair[k])
            elif dist <= 2*T:
                unfair[i] = min(unfair[i], C[k] + fair[k])

    return unfair[n - 1]
