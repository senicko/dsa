from zad1testy import runtests

"""
Złożoność czasowa: O(nk)

PS. Radix sort działa słabo dla bardzo długich napisów, dlatego
    Testy sprawdzające wydajność dla takich przypadków mielą i mają
    problem.
"""


def bucket_sort(T, pos):
    buckets = [[] for _ in range(26)]

    for word in T:
        idx = ord(word[pos]) - ord('a') if pos < len(word) else 0
        buckets[idx].append(word)

    i = 0

    for bucket in buckets:
        for j in range(len(bucket)):
            T[i] = bucket[j]
            i += 1


def radix_sort(T):
    k = -1
    for word in T:
        k = max(k, len(word))

    for i in range(k):
        bucket_sort(T, i)


def strong_string(T):
    n = len(T)

    for i in range(n):
        rev = T[i][::-1]
        if rev < T[i]:
            T[i] = rev

    radix_sort(T)

    max_strength = 0
    current_strength = 1
    prev = T[0]

    for i in range(1, n):
        if T[i] == prev:
            current_strength += 1
        else:
            max_strength = max(max_strength, current_strength)
            current_strength = 1
            prev = T[i]

    return max(max_strength, current_strength)


# Odkomentuj by uruchomic duze testy
runtests(strong_string, all_tests=True)

# Zakomentuj gdy uruchamiasz duze testy
# runtests(strong_string, all_tests=False)
