''' 
Minimum Spanning Tree MST select min cost vertex but no cycle will be formed.
We have to select minimum cost edge but make sure next vertex must me connected to selected one.

The time complexity of Prim's algorithm for finding the Minimum Spanning Tree 
(MST) of an undirected weighted graph is O(E log V), where E is the number of 
edges and V is the number of vertices in the graph.
'''
import heapq


def prims_algo(N, graph, start):

    adj = {i: [] for i in range(N + 1)}

    for u, v, d in graph:  # list of [cost and node]
        adj[u].append([d, v])
        adj[v].append([d, u])

    dist = {i: float("inf") for i in range(N)}
    dist[start] = 0

    # need parent array so that will always
    parent = [-1] * N

    visit = set([(start)])
    minHeap = [[0, start]]

    while minHeap:

        d, node = heapq.heappop(minHeap)

        for nei_dist, nei in adj[node]:

            if nei not in visit and dist[nei] > nei_dist:

                visit.add(node)

                parent[nei] = node

                dist[nei] = nei_dist

                heapq.heappush(minHeap, [nei_dist, nei])

    return dist


# Undirected Graph Example
graph = [[0, 1, 2], [0, 3, 6], [1, 2, 3], [1, 3, 8], [1, 4, 5], [2, 4, 7]]

print(prims_algo(5, graph, 0))
