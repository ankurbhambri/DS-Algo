# https://leetcode.com/problems/sum-of-distances-in-tree/submissions/1861529283/

# Similar - https://cses.fi/problemset/task/1133/

# Sum of Distances (Simple Rerooting)

from collections import defaultdict


class Solution(object):
    def sumOfDistancesInTree(self, N, edges):

        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        size = [1] * N
        dp = [0] * N
        ans = [0] * N

        # First DFS: subtree sizes + subtree distances
        def dfs(node = 0, parent = None):

            for child in graph[node]:

                if child != parent:

                    dfs(child, node)

                    size[node] += size[child]

                    dp[node] += dp[child] + size[child]
    
        # Second DFS: rerooting to calculate distances for all nodes
        def dfs2(node = 0, parent = None):

            for child in graph[node]:

                if child != parent:
                    
                    # one step closer to child, one step farther from all other nodes
                    ans[child] = ans[node] - size[child] + N - size[child]

                    dfs2(child, node)

        dfs()
        ans[0] = dp[0]
        dfs2()

        return ans

print(Solution().sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))