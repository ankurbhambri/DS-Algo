# https://leetcode.com/problems/critical-connections-in-a-network

from collections import defaultdict


# TC: O(V + E), SC: O(V + E)

# Find the bridges in a graph using Tarjan's algorithm. A bridge is an edge that, if removed, will increase the number of connected components in the graph.
class Solution:
    def criticalConnections(self, n, connections):

        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        timer = 0

        bridges = []

        low = [0] * n

        disc = [-1] * n

        def dfs(u, parent):

            nonlocal timer

            disc[u] = low[u] = timer

            timer += 1

            for v in graph[u]:

                if v == parent:
                    continue

                if disc[v] == -1:

                    dfs(v, u)

                    low[u] = min(low[u], low[v])

                    if low[v] > disc[u]:
                        bridges.append([u, v])

                else:
                    low[u] = min(low[u], disc[v])

        dfs(0, -1)

        return bridges


print(Solution().criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))   # Output: [[1, 3]]
print(Solution().criticalConnections(5, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]))   # Output: [[3, 4]]