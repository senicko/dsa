"""
Wyszukiwanie maksymalnego skojarzenia w grafie korzystając z DFS

Bardzo spoko artykuł na Geeks For Geeks
https://www.geeksforgeeks.org/maximum-bipartite-matching/
"""


def maximum_bipartite_matching(graph, jobs):
    n = len(graph)
    job_worker = [None] * jobs

    def bpm(worker, visited):
        for job in graph[worker]:
            if not visited[job]:
                visited[job] = True

                if job_worker[job] is None or bpm(job_worker[job], visited):
                    job_worker[job] = worker
                    return True

        return False

    result = 0

    for worker in range(n):
        visited = [False] * jobs

        if bpm(worker, visited):
            result += 1

    return result


if __name__ == "__main__":
    # Input graph is represented as Edmonds Matrix.
    # Each row can be understood as worker,
    # and each array as a list of machines (jobs) they can use.

    jobs = 5

    graph = [
        [0, 1],  # Worker 0 can do Job 0 and Job 1
        [1, 2],
        [0, 3],
        [3, 4]
    ]

    print(maximum_bipartite_matching(graph, jobs))
