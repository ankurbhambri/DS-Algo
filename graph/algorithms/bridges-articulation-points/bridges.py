################ Tarjan's Algorithm to find bridges in a graph #################

from collections import defaultdict

# TC: O(V + E), SC: O(V + E)
class Solution:
    def findBridges(self, n, connections):

        graph = defaultdict(list)

        # Undirected graph banao
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # disc[node] = node pehli baar kis time visit hua
        disc = [-1] * n

        # low[node] = meri subtree sabse purane kis node tak pahunch sakti hai
        low = [-1] * n

        timer = 0
        bridges = []

        def dfs(node, parent):

            nonlocal timer

            # Discovery aur low dono initially same hote hain
            disc[node] = low[node] = timer
            timer += 1

            for nei in graph[node]:

                # Parent wali edge ko ignore karo
                if nei == parent:
                    continue

                # Agar neighbor abhi tak visit nahi hua to DFS lagao
                if disc[nei] == -1:

                    dfs(nei, node)

                    # DFS se wapas aane ke baad child ka low value propagate karo
                    low[node] = min(low[node], low[nei])

                    # Agar child ki subtree parent ya uske ancestors tak
                    # kisi aur path se nahi pahunch sakti, to ye edge bridge hai
                    if low[nei] > disc[node]:
                        bridges.append([node, nei])

                # Neighbor already visit ho chuka hai aur parent bhi nahi hai,
                # iska matlab ye back-edge hai.
                # Is back-edge ki wajah se hum kisi purane node tak pahunch sakte hain.
                else:
                    low[node] = min(low[node], disc[nei])

        # Graph disconnected bhi ho sakta hai,
        # isliye har component se DFS start karo
        for i in range(n):
            if disc[i] == -1:
                dfs(i, -1)

        return bridges


print(Solution().findBridges(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))   # Output: [[1, 3]]
print(Solution().findBridges(5, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]))   # Output: [[3, 4]]


# https://leetcode.com/problems/critical-connections-in-a-network


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

        # yha pe start node 0 se dfs call kar rahe hai, aur parent ko -1 pass kar rahe hai, kyunki start node ka koi parent nahi hai.
        dfs(0, -1)

        return bridges


print(Solution().criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))   # Output: [[1, 3]]
print(Solution().criticalConnections(5, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]))   # Output: [[3, 4]]