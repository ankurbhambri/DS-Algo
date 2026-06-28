"""
https://www.geeksforgeeks.org/maximum-number-of-edges-to-be-removed-to-contain-exactly-k-connected-components-in-the-graph/

Given an undirected graph G with N nodes, M edges, and an integer K, the task is to find the maximum count of edges that can be removed such that there
remains exactly K connected components after the removal of edges. If the graph cannot contain K connect components, print -1.

Given an undirected graph with n nodes and m edges, where each edge has a weight w_i.

Find the minimum number of edges that need to be removed to disconnect the graph into exactly k connected components.

"""

class Solution:
    def max_edges_to_remove(self, N, M, K, Edges):

        # Impossible to have more components than nodes
        if K > N:
            return -1

        adj = {i: [] for i in range(N + 1)}

        for u, v in Edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(node):
            visit.add(node)
            for child in adj[node]:
                if child not in visit:
                    dfs(child)

        c = 0 # Initial connected components count

        # Saare nodes par loop chalakar components count karenge
        for i in range(N):
            if i not in visit:
                c += 1
                dfs(i)

        # Agar initial components K se zyada hain, toh K components banana impossible hai
        if c > K:
            return -1

        # Formula apply karenge: M - N + K
        return M - N + K


N = 4
M = 3
K = 2
Edges = [[1, 2], [2, 3], [3, 4]]
print(Solution().max_edges_to_remove(N, M, K, Edges)) # Output: 1

N = 3
M = 3
K = 3
Edges = [[1, 2], [2, 3], [3, 1]]
print(Solution().max_edges_to_remove(N, M, K, Edges)) # Output: 3


"""
EXPLANATION:

## 📌 Maximum Edges Removed to get Exactly K Connected Components

### Step 1: Initial connected components = C
    - Find number of connected components using DFS/BFS
    - If C > K → Impossible (-1)
    - Reason: Edge removal cannot merge components, only increases their count

### Step 2: Minimum edges needed for K connected components
    - A tree with x nodes has (x - 1) edges
    - If component sizes are a1, a2, ..., aK
    - Minimum edges = (a1-1) + (a2-1) + ... + (aK-1) = N - K
    - Minimum edges to keep = N - K

### Step 3: Maximum removable edges
    - Initially: M edges
    - Need to keep: N - K edges
    - Maximum removable = M - (N - K) = M - N + K

### Formula:
    If C > K:
        Answer = -1
    Else:
        Answer = M - N + K

### Key Insight:
    Final graph with K components is a forest with exactly (N - K) edges.
    Therefore: Maximum removable = M - (N - K) = M - N + K
"""