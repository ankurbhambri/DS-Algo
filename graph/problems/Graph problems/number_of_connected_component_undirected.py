# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

class Solution:
    def countComponents(self, n: int, edges):
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()

        def dfs(node):
            visit.add(node)
            for child in adj[node]:
                if child not in visit:
                    dfs(child)
        res = 0
        for i in range(n):
            if i not in visit:
                res += 1
                dfs(i)
        return res
