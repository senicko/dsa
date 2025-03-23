def dominance(P):
    n = len(P)

    # Each coordinate will store number of points
    # with coordinate greater or equal to it.
    x = [0] * (n + 1)
    y = [0] * (n + 1)

    for p in P:
        x[p[0]] += 1
        y[p[1]] += 1

    for i in range(n - 1, -1, -1):
        x[i] += x[i + 1]
        y[i] += y[i + 1]

    min_not_dominated = float("inf")

    for p in P:
        # This counts |x| + |y| + |x ∩ y| Every point with
        # both x and y greater equal will be counted twice. This
        # is not a problem however as the point which dominates
        # most points can't have any point in area |x ∩ y|.
        not_dominated = x[p[0]] + y[p[1]]
        min_not_dominated = min(min_not_dominated, not_dominated)

    # The point dominating most points counted itself twice,
    # because of adding |x ∩ y|, So we need to subtract 1.
    return n - (min_not_dominated + 1)
