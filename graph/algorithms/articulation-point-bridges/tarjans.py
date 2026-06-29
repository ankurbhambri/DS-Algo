def find_bridges_and_articulation_points(graph, n):

    timer = 0
    disc = [-1] * n
    low = [0] * n
    visited = [False] * n
    bridges = []
    articulation = [False] * n

    def dfs(u, parent):

        nonlocal timer

        visited[u] = True
        disc[u] = low[u] = timer
        timer += 1

        children = 0

        for v in graph[u]:
            
            # case 1: if neighbor v is parent of u, then ignore it
            if v == parent:
                continue
            
            # case 2: neighbor v is not visited yet
            if not visited[v]:

                children += 1

                dfs(v, u)

                low[u] = min(low[u], low[v])

                # Bridge
                if low[v] > disc[u]:
                    bridges.append((u, v))

                # Articulation Point (non-root)
                if parent != -1 and low[v] >= disc[u]:
                    articulation[u] = True

            # case 3: neighbor v is already visited (back edge)
            else:
                low[u] = min(low[u], disc[v])

        # Root case
        if parent == -1 and children > 1:
            articulation[u] = True


print(find_bridges_and_articulation_points({0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}, 4))   # Output: ([(2, 3)], [False, False, True, False])
print(find_bridges_and_articulation_points({0: [1], 1: [0, 2, 3], 2: [1], 3: [1]}, 4))   # Output: ([(1, 2), (1, 3)], [False, True, False, False])


# https://leetcode.com/problems/critical-connections-in-a-network

from collections import defaultdict

# TC: O(V + E), SC: O(V + E)
class Solution:
    def criticalConnections(self, n, connections):

        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n
        low = [0] * n
        timer = 0
        bridges = []

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