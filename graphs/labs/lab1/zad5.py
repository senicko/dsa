def find_universal_brute(graph):
    n = len(graph)
    zero_counts = [0] * n
    one_counts = [0] * n

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                zero_counts[i] += 1
            else:
                one_counts[j] += 1

    for i in range(n):
        if zero_counts[i] == n and one_counts[i] == n - 1:
            return i

    return -1


def find_universal(graph):
    n = len(graph)
    i = 0
    j = 0

    while i < n and j < n:
        if graph[i][j] == 0:
            j += 1
        else:
            i += 1

    if j == n:
        j -= 1
        count = 0

        for k in range(n):
            if graph[k][i] == 1:
                count += 1

        if count == n - 1:
            return i

    return -1


if __name__ == "__main__":
    graph = [
        [0, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 0, 1],
        [1, 1, 1, 0],
    ]

    print(find_universal(graph))
    print(find_universal_brute(graph))
