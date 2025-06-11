"""
Zależność rekurencyjna:


    T(i, k) = Najlepsza wartość podział przedziału [:i] po wykonaniu k podziałów.


    T(i, k) = max(
        // Wybieramy punkt kolejnego podziału (ostatni element, który będzie do niego należał)
        for s in range(i, n):
            min(
                sum(A[i:s + 1]),
                T(s + 1, k - 1)
            )
        )


Złożoność:
    - O(nk) pod-problemów.
    - Rozwiązanie każdego podproblemu zajmuje O(n).
    - Zakładamy że mamy sumy prefiksowe, więc sumowanie działa w O(1)

    Finalna złożoność: O(n^2 * k)
"""


from math import inf


def maximin_top_down_aux(a, i, k, cache):
    # If we have used all value, or we
    # can't create more partitions.
    if i == len(a) or k == 0:
        return -inf

    # This is the last partition, so it's
    # best value is just it's sum.
    if k == 1:
        return sum(a[i:])

    # The result might be already cached.
    if cache[i][k] > -1:
        return cache[i][k]

    n = len(a)
    result = -inf

    for s in range(i, n):
        result = max(
            result,
            min(
                sum(a[i:s + 1]),
                maximin_top_down_aux(a, s + 1, k - 1, cache)
            )
        )

    cache[i][k] = result

    return result


def maximin_top_down(a, k):
    cache = [[-inf] * (k + 1) for _ in range(len(a))]
    return maximin_top_down_aux(a, 0, k, cache)


def maximin_bottom_down(a, k):
    n = len(a)

    dp = [[-inf] * (k + 1) for _ in range(n + 1)]
    prefix_sum = [0] * (n + 1)

    for i in range(n):
        prefix_sum[i] = prefix_sum[i - 1] + a[i]

    for i in range(n):
        dp[i][1] = sum(a[i:])

    for i in range(n - 1, -1, -1):
        for p in range(2, k + 1):
            result = -inf

            for s in range(n - 1, i - 1, -1):
                result = max(
                    result,
                    min(
                        prefix_sum[s] - prefix_sum[i - 1],
                        dp[s + 1][p - 1]
                    )
                )

            dp[i][p] = result

    return dp[0][k]


if __name__ == "__main__":
    a = [4, 2, 7, 1, 3, 5, 9]
    k = 3
    result = maximin_top_down(a, k)
    assert result == maximin_bottom_down(a, k)
    print(f"OK, result={result}")
