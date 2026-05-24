# https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

from collections import deque

class Solution:
    def minOperationsQueries(self, n: int, edges, queries):

        LOG = 15  # since n <= 1e4

        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # parent[k][x] = 2^k ancestor of x
        parent = [[-1] * n for _ in range(LOG)]

        depth = [0] * n

        # cnt[x][w] = frequency of weight w from root -> x
        cnt = [[0] * 27 for _ in range(n)]

        # BFS / DFS
        q = deque([0])
        visited = [False] * n
        visited[0] = True

        while q:
            node = q.popleft()

            for nei, wt in graph[node]:

                if visited[nei]:
                    continue

                visited[nei] = True

                depth[nei] = depth[node] + 1
                parent[0][nei] = node

                cnt[nei] = cnt[node][:]   # copy frequencies
                cnt[nei][wt] += 1

                q.append(nei)

        # binary lifting table
        for k in range(1, LOG):
            for node in range(n):

                p = parent[k - 1][node]

                if p != -1:
                    parent[k][node] = parent[k - 1][p]

        def lca(u, v):

            if depth[u] < depth[v]:
                u, v = v, u

            # lift u
            diff = depth[u] - depth[v]

            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            # lift both
            for k in range(LOG - 1, -1, -1):

                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        ans = []

        for u, v in queries:

            l = lca(u, v)

            path_len = depth[u] + depth[v] - 2 * depth[l]

            mx = 0

            for w in range(1, 27):

                freq = (
                    cnt[u][w]
                    + cnt[v][w]
                    - 2 * cnt[l][w]
                )

                mx = max(mx, freq)

            ans.append(path_len - mx)

        return ans
