"""
T(i) = największa liczba sztabek przy wejściu do komnaty i

T(i) = max(
    for k in parents(i):
        T(k) + gold_diff
)
"""


def magic( C ):
    n = len(C)
    gold = [-1] * n
    gold[0] = 0

    for i in range(n):
        if gold[i] == -1:
            continue

        g = C[i][0]
        caves = C[i][1:]

        picked_gold = min(g, 10)
        g -= picked_gold

        for k, w in caves:
            if w == -1 or k < g:
                continue

            current_gold = gold[i] + picked_gold - (k - g)
            gold[w] = max(gold[w], current_gold)

    return gold[n - 1]
