"""
Pokrycie kolorów.

Mamy tablicę T, z n elementami.

Wartości tablicy to kolory od 0 do k - 1. Szukamy najkrótszego przedziału od i do j takiego, że elementy w tym przedziale
zawierają wszystkie kolory, w dowolnej kolejności.
"""

from random import randint


def color_coverage(T, k):
    n = len(T)

    counts = [0] * k
    unique = 0

    start = 0
    end = 0

    min_window = float("inf")

    while end < n:
        # Increment count of current color.
        counts[T[end]] += 1

        # If it's first color of this type in our window,
        # inc unique count.
        if counts[T[end]] == 1:
            unique += 1

        # Inc end index.
        end += 1

        # Wile we have k unique colors.
        while unique == k:
            # Take min of old min and current window.
            min_window = min(min_window, end - start)

            # Dec count of color coming out of current window.
            counts[T[start]] -= 1

            # If count of the color fell down to 0,
            # dec unique.
            if counts[T[start]] == 0:
                unique -= 1

            # Inc start index.
            start += 1

    return min_window


if __name__ == "__main__":
    k = 5
    T = [randint(0, k - 1) for _ in range(10)]
    print(T)
    print(color_coverage(T, k))
