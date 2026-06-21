"""
A Bipartite graph is a graph whose vertices can be divided into two disjoint sets.
To check graph is Bipartite or not we represent vertices with color but condition is 
an adjacent node cannot be of same color is 0 then child must be 1.
"""

from collections import deque

# DFS
# Time complexity: O(V + E)
# Space complexity: O(V)

class Solution:
    def isBipartite(self, graph):

        n = len(graph)

        color = [-1] * n      # -1 = unvisited

        for start in range(n):

            if color[start] != -1:
                continue

            q = deque([start])
            color[start] = 0

            while q:

                node = q.popleft()

                for nei in graph[node]:

                    if color[nei] == -1:

                        color[nei] = 1 - color[node]
                        q.append(nei)

                    elif color[nei] == color[node]:
                        return False

        return True


print(Solution().isBipartite([[1,3], [0,2], [1,3], [0,2]]))  # True
print(Solution().isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))  # False