# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i

class Solution:
    def maxTargetNodes(self, edges1, edges2, k):

        def dfs(node, visited, adj, k):

            if k < 0:
                return 0
            res = 1
            visited[node] = True
            for child in adj[node]:
                if not visited[child]:
                    res += dfs(child, visited, adj, k - 1)
            return res

        def build(edges, k):

            n = len(edges) + 1
            adj = [[] for _ in range(n)]

            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)

            res = [0] * n
            for i in range(n):
                visited = [False] * n
                res[i] = dfs(i, visited, adj, k)

            return res

        n = len(edges1) + 1

        # counting reachable node from every node till k level
        count1 = build(edges1, k)
        count2 = build(edges2, k - 1)

        maxCount2 = max(count2)

        res = [count1[i] + maxCount2 for i in range(n)]

        return res

print(Solution().maxTargetNodes([[0,1],[0,2],[2,3],[2,4]], [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], 2))
