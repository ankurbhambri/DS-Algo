'''Shortest path algorithm works may work in negative weights or may not
It runs only one iterations - o(n^2) best and worst o(n^3)'''

import heapq
from collections import defaultdict


def dijkstra(graph, n, k):

    adj = defaultdict(list)

    for u, v, w in graph:
        adj[u].append((v, w))

    visit = set()

    minHeap = [(0, k)]

    res = 0

    while minHeap:

        w1, n1 = heapq.heappop(minHeap)

        if n1 in visit:
            continue

        visit.add(n1)
        res = max(res, w1)

        for n2, w2 in adj[n1]:
            if n2 not in visit:
                heapq.heappush(minHeap, (w1 + w2, n2))

    return res if len(visit) == n else -1


# graph = [2 (U), 1 (V), 1 (Weight)]
print(dijkstra(graph=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
