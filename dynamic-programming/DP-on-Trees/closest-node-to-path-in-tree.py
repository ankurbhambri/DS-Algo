# https://leetcode.com/problems/closest-node-to-path-in-tree/description/

from collections import deque

class Solution:
    def closestNode(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = 15  # Kyunki n <= 10000 generally, 2^14 = 16384
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        
        # 2. BFS se depth aur parents nikalyein
        queue = deque([0])
        visited = [False] * n
        visited[0] = True
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    up[v][0] = u
                    queue.append(v)
                    
        # 3. Binary Lifting table fill karein
        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j - 1]][j - 1]
                
        # 4. Standard LCA function
        def get_lca(u: int, v: int) -> int:

            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(LOG):

                if (diff >> j) & 1:
                    u = up[u][j]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]

            return up[u][0]

        # 5. Queries process karein
        ans = []
        for start, end, node in queries:

            # Teeno combinations ke LCAs nikalein
            lca1 = get_lca(start, end)
            lca2 = get_lca(start, node)
            lca3 = get_lca(end, node)

            # Jis LCA node ki depth sabse zyada hai, wahi closest hai
            best_node = lca1
            if depth[lca2] > depth[best_node]:
                best_node = lca2

            if depth[lca3] > depth[best_node]:
                best_node = lca3

            ans.append(best_node)

        return ans