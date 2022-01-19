''' Minimum Spanning Tree MST Select minimum vertex but no cycle will be formed '''

import heapq


def prims(N, graph):

    adj = {i: [] for i in range(N + 1)}

    for u, v, d in graph:  # list of [cost and node]
        adj[u].append([d, v])
        adj[v].append([d, u])

    res = 0
    visit = set()
    minHeap = [[0, 1]]

    # BFS
    while minHeap:

        d, v = heapq.heappop(minHeap)
        if v in visit:
            continue
        res += d
        visit.add(v)
        for d1, nei in adj[v]:
            if nei not in visit:
                heapq.heappush(minHeap, [d1, nei])

    return res


# Undirectd Graph Example
graph = [
    [1, 2, 1],
    [2, 3, 4],
    [3, 4, 1],
    [4, 5, 2],
    [1, 5, 3],
    [2, 5, 2],
    [2, 4, 1],
]

print(prims(5, graph))