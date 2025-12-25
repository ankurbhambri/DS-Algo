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

print(Solution().sumOfDistancesInTree(6, [[0, 1],[0, 2],[2, 3],[2, 4],[2, 5]]))


# https://codeforces.com/contest/1092/problem/F

import sys
sys.setrecursionlimit(10 ** 7)
from collections import defaultdict

# Here, the difference is each node has a weight/val associated with it, and instead of capturing the size we capture the weight sums.
def solution(edges, n, vals):

    adj = defaultdict(list)

    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    wt = [0] * n       # subtree weights
    dp = [0] * n       # subtree cost
    ans = [0] * n

    def dfs(u = 0, p = -1):

        wt[u] = vals[u]
        dp[u] = 0

        for v in adj[u]:

            if v == p:
                continue

            dfs(v, u)

            wt[u] += wt[v]
            dp[u] += dp[v] + wt[v]

    def dfs2(u = 0, p = -1):
        for v in adj[u]:

            if v == p:
                continue

            ans[v] = ans[u] - wt[v] + (totalWeight - wt[v])

            dfs2(v, u)

    dfs()
    totalWeight = wt[0]
    ans[0] = dp[0]
    dfs2()

    return ans

print(max(solution([(1, 2),(1, 5),(1, 4),(2, 3),(5, 6),(5, 7),(5, 8)], 8, [9, 4, 1, 7, 10, 1, 6, 5])))  # Output: 121