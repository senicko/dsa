"""
Mamy tablicę T, w której znajduje się `n` elementów.
Szukamy elementów `x` i `y` takich, że różnica między nimi jest największa ze wszystkich par,
oraz nie istnieje element `z` taki, że `x` < `z` < `y`.

Na przykład
    T = [1, 4, 2, 8, 3, 9, 2]
    max_diff(T) -> (4, 8)

_Dlaczego? W tablicy nie ma elementów [5, 6, 7], więc para (4, 8) jest prawidłowa,
i jednocześnie ich różnica jest największa ze wszystkich takich prawidłowych par.

Para (4, 9) nie jest prawidłowa, ponieważ w tablicy jest 8._
"""


def max_diff(T):
    n = len(T)
    buckets = [[float("inf"), float("-inf")] for _ in range(n)]

    low, high = min(T), max(T)
    span = high - low

    for value in T:
        bucket_index = int(((value - low) / span) * (n - 1))
        buckets[bucket_index][0] = min(buckets[bucket_index][0], value)
        buckets[bucket_index][1] = max(buckets[bucket_index][1], value)

    result_low = 0
    result_high = 0
    prev_low = buckets[0][0]

    for i in range(1, n):
        # Skip empty spans.
        if buckets[i][0] == float("inf"):
            continue

        if result_high - result_low < buckets[i][1] - prev_low:
            result_low = prev_low
            result_high = buckets[i][1]

        prev_low = buckets[i][0]

    return result_low, result_high


if __name__ == "__main__":
    a = [1, 4, 2, 8, 3, 9, 2]
    print(max_diff(a))
