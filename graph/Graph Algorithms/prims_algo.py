''' 
Minimum Spanning Tree MST select min cost vertex but no cycle will be formed.
We have to select minimum cost edge but make sure next vertex must me connected to selected one.
'''
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

        cost, v = heapq.heappop(minHeap)
        if v in visit:
            continue
        res += cost
        visit.add(v)
        for new_cost, nei in adj[v]:
            if nei not in visit:
                heapq.heappush(minHeap, [new_cost, nei])

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
