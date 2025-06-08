def set_sum_aux(values, i, s, cache):
    if s == 0:
        return True

    if i == len(values):
        return False

    if cache[i][s] is None:
        return cache[i][s]

    result = set_sum_aux(values, i + 1, s, cache)

    if values[i] <= s:
        result = result or set_sum_aux(values, i + 1, s - values[i], cache)

    cache[i][s] = result
    return result


def set_sum(values, s):
    cache = [[None] * (s + 1) for _ in range(len(values))]
    return set_sum_aux(values, 0, s, cache)
