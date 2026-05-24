# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        queue = deque([(1, 0)]) 
        visited = {1}

        max_depth = 0

        while queue:

            u, d = queue.popleft()

            if d > max_depth:
                max_depth = d
            
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append((v, d + 1))

        # L hamari maximum edge length hai
        L = max_depth
        MOD = 10**9 + 7

        return (2 ** (L - 1)) % MOD if L != 0 else 0


# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/


class Solution:
    def assignEdgeWeights(self, edges: list[list[int]], queries: list[list[int]]) -> list[int]:

        max_node = 1
        for u, v in edges:
            if u > max_node:
                max_node = u
            if v > max_node:
                max_node = v
            
        n = max_node
        LOG = 18  # Kyunki n <= 10^5, 2^17 = 131072 (> 100000)

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # up[node][j] store karega node ka 2^j-th ancestor
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)

        # 3. BFS se depth aur immediate parent nikalyein (Starting from root 1)
        queue = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True

        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    up[v][0] = u  # v ka immediate parent u hai
                    queue.append(v)

        # 4. Binary Lifting table (up) ko fill karein
        for j in range(1, LOG):
            for i in range(1, n + 1):
                # Agar parent valid hai tabhi uska dada/paddada nikalenge
                if up[i][j - 1] != 0:
                    up[i][j] = up[up[i][j - 1]][j - 1]

        # 5. Fast LCA function using Binary Lifting
        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u

            # Dono ko same depth par lao
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]

            if u == v:
                return u

            # Dono ko ek saath upar le jao
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]

            return up[u][0]

        # 6. Queries ko process karein
        MOD = 10**9 + 7
        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)  # Same node matlab 0 edges -> Cost = 0 (Even)
                continue

            lca = get_lca(u, v)
            # Path Length (Total Edges)
            L = depth[u] + depth[v] - 2 * depth[lca]

            # Formula: 2^(L - 1) % MOD
            ans.append(pow(2, L - 1, MOD))

        return ans