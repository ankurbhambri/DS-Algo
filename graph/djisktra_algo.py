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
        # weight, node
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


import math


class Solution:
    def minCost(self, maxTime, edges, passingFees):
        n = len(passingFees)
        graph = [[] for _ in range(n)]
        for x, y, t in edges:
            graph[x].append((y, t))
            graph[y].append((x, t))
        cost = [math.inf] * n  # cost[i] := min cost to reach cities[i]
        time = [math.inf] * n  # time[i] := min cost to reach cities[i]
        minHeap = []  # (cost, time, node)

        # start with node 0 with cost = time = 0
        heapq.heappush(minHeap, (passingFees[0], 0, 0))
        cost[0] = passingFees[0]
        time[0] = 0

        while minHeap:
            currCost, currTime, x = heapq.heappop(minHeap)
            for y, pathTime in graph[x]:
                if currTime + pathTime <= maxTime:
                    # go from x -> y
                    newCost = currCost + passingFees[y]
                    newTime = currTime + pathTime
                    if cost[y] > newCost:
                        cost[y] = newCost
                        time[y] = newTime
                        heapq.heappush(minHeap, (newCost, newTime, y))
                    elif time[y] > newTime:
                        time[y] = newTime
                        heapq.heappush(minHeap, (newCost, newTime, y))

        return -1 if cost[-1] == math.inf else cost[-1]
