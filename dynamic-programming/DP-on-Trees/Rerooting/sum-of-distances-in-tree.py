# https://leetcode.com/problems/sum-of-distances-in-tree/submissions/1861529283/

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



# Max Distance / Tree Distances (Prefix-Suffix Rerooting)

import sys
sys.setrecursionlimit(200005)

def solve_max_dist():
    n = int(input())
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    height = [0] * n

    # DFS 1: Har node ki niche ki max height nikal lo
    def dfs1(u, p):
        curr_h = 0
        for v in adj[u]:
            if v == p: continue
            dfs1(v, u)
            curr_h = max(curr_h, 1 + height[v])
        height[u] = curr_h

    ans = [0] * n

    # DFS 2: Rerooting with Prefix/Suffix
    def dfs2(u, p, top_dist):
        ans[u] = max(height[u], top_dist)

        # Children ki heights gather karo
        children = []
        for v in adj[u]:
            if v != p:
                children.append((v, height[v]))
        
        m = len(children)
        if m == 0: return

        # Prefix aur Suffix Max arrays
        pref = [0] * (m + 1)
        suff = [0] * (m + 1)
        
        for i in range(m):
            pref[i+1] = max(pref[i], 1 + children[i][1])
        for i in range(m-1, -1, -1):
            suff[i] = max(suff[i+1], 1 + children[i][1])

        # Har child par reroot karo
        for i in range(m):
            v = children[i][0]
            # Max of: top se aane wala, left siblings, aur right siblings
            max_for_child = max(top_dist + 1, pref[i] + 1, suff[i+1] + 1)
            dfs2(v, u, max_for_child)

    dfs1(0, -1)
    dfs2(0, -1, 0)
    print(*(ans))

# solve_max_dist()
