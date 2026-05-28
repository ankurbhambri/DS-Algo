from collections import deque


class Solution:
    def minOperationsQueries(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:

        # 1. Graph (Adjacency List) taiyar karein
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        LOG = 15  # Kyunki n <= 10^4 aur 2^14 = 16384 (> 10000)

        # Binary lifting ke liye up table: up[node][j] stores 2^j-th ancestor
        up = [[0] * LOG for _ in range(n)]
        # Root se har node tak ke edge weights ki frequency (1 se 26 tak)
        freq = [[0] * 27 for _ in range(n)]
        depth = [0] * n

        # 2. Iterative BFS se depth aur frequency table fill karein
        queue = deque([0])
        visited = [False] * n
        visited[0] = True

        while queue:
            u = queue.popleft()
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    depth[v] = depth[u] + 1
                    up[v][0] = u

                    # Parent ki frequencies copy karein aur current edge weight ko badhayein
                    freq[v] = list(freq[u])
                    freq[v][w] += 1

                    queue.append(v)

        # 3. Binary Lifting table (up) ko complete karein
        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j - 1]][j - 1]

        # 4. LCA (Lowest Common Ancestor) nikalne ka function
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            # Dono nodes ko pehle same depth par lekar aao
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]

            if u == v:
                return u

            # Dono ko ek saath upar le jao jab tak unka parent same na ho jaye
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]

            return up[u][0]

        # 5. Har query ko solve karein
        ans = []
        for a, b in queries:

            max_freq = 0
            lca = get_lca(a, b)

            # Total edges between a and b
            total_edges = depth[a] + depth[b] - 2 * depth[lca]

            # 1 se 26 tak loop chalakar check karein kis weight ki frequency sabse zyada hai
            for w in range(1, 27):
                current_freq = freq[a][w] + freq[b][w] - 2 * freq[lca][w]
                if current_freq > max_freq:
                    max_freq = current_freq

            # Operations = Total Edges - Max Frequency
            ans.append(total_edges - max_freq)

        return ans