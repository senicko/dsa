def binworker(M):
    # no. workers
    n = len(M)

    # no. machines
    m = max(map(max, M)) + 1

    machine_worker = [None] * m

    def bpm(worker, visited):
        for machine in M[worker]:
            if not visited[machine]:
                visited[machine] = True

                if machine_worker[machine] is None or bpm(machine_worker[machine], visited):
                    machine_worker[machine] = worker
                    return True

        return False

    result = 0

    for worker in range(n):
        visited = [False] * m

        if bpm(worker, visited):
            result += 1

    return result
