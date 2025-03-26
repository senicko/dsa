def cesar(s):
    n = len(s)
    res = 1

    for i in range(n):
        for j in range(n):
            l = i - j
            r = i + j

            # Expand left and right.
            if l < 0 or r >= n or s[l] != s[r]:
                break

            res = max(res, r - l + 1)

    return res
