'''Shortest path algorithm works may work in negative weights or may not
It runs only one iterations - o(n^2) best and worst o(n^3)'''

import heapq
import math
from collections import defaultdict

'''
TC nlogn with priority queue aka Min Heap 
TC worst case is n^2 in case of n vertices processed and n vertex relaxed
'''


def dijkstra(graph, N, start):

    adj = defaultdict(list)

    for u, v, w in graph:
        adj[u].append((v, w))

    dist = {i: float("inf") for i in range(N)}

    dist[start] = 0

    minHeap = [(0, start)]  # weight, node

    while minHeap:
        # weight, node
        weight, node = heapq.heappop(minHeap)

        '''
        However, the check if dist > distances[current_node]: continue is still
        included as an optimization to improve the algorithm's efficiency.
        The reason is that when a node is added to the priority queue with a
        certain tentative distance, there may be other nodes in the queue with
        smaller tentative distances to the same node. These nodes may be processed
        later and update the distance to the same node, resulting in a shorter path.

        If we did not skip the node in the check, we would process the node again
        with a longer distance, which would not result in a shorter path and would
        slow down the algorithm unnecessarily. By skipping the node if its distance
        is already smaller than the tentative distance in the priority queue, we
        avoid processing it again and guarantee that we have found the shortest
        path to that node.

        So the check if dist > distances[current_node]: continue is a way to ensure
        that we are only processing each node once and that we are finding the
        shortest path to each node, while avoiding unnecessary computations and
        speeding up the algorithm.
        '''

        if weight > dist[node]:
            continue

        for child, child_weight in adj[node]:

            new_dist = dist[node] + child_weight

            if dist[child] > new_dist:

                dist[child] = new_dist

                heapq.heappush(minHeap, (new_dist, child))

    return dist


# graph = [2 (U), 1 (V), 1 (Weight)]
print(
    dijkstra(
        [[1, 2, 5], [1, 3, 2], [2, 4, 4], [3, 2, 1], [3, 4, 4]], N=5, start=1
    )
)  # o/p {1: 0, 2: 3, 3: 2, 4: 6}


# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/
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
            currCost, currTime, node = heapq.heappop(minHeap)

            for child, pathTime in graph[node]:

                if currTime + pathTime <= maxTime:

                    newCost = currCost + passingFees[child]
                    newTime = currTime + pathTime

                    if cost[child] > newCost:
                        cost[child] = newCost
                        time[child] = newTime
                        heapq.heappush(minHeap, (newCost, newTime, child))

                    elif time[child] > newTime:
                        time[child] = newTime
                        heapq.heappush(minHeap, (newCost, newTime, child))

        return -1 if cost[-1] == math.inf else cost[-1]


# More Problems
# https://leetcode.com/problems/the-maze/
# https://leetcode.com/problems/the-maze-ii/
# https://leetcode.com/problems/the-maze-iii/
