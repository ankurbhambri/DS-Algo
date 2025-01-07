"""
https://www.geeksforgeeks.org/maximum-number-of-edges-to-be-removed-to-contain-exactly-k-connected-components-in-the-graph/

Given an undirected graph G with N nodes, M edges, and an integer K, the task is to find the maximum count of edges that can be removed such that there
remains exactly K connected components after the removal of edges. If the graph cannot contain K connect components, print -1.

Given an undirected graph with n nodes and m edges, where each edge has a weight w_i, find the minimum number of edges that need to be removed to disconnect the graph into exactly k connected components.

"""


def max_edges_to_remove(N, M, K, Edges):

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

    c = 0
    for i in range(N):
        if i not in visit:
            c += 1
            dfs(i)

    # No edges need to be removed
    if K <= c:
        return 0

    if c <= K:
        return (
            M - N + K
        )  # N is the number nodes, M is the number of edges and K is the required number of connected components.

    return -1


N = 4
M = 3
K = 2
Edges = [[1, 2], [2, 3], [3, 4]]
print(max_edges_to_remove(N, M, K, Edges))

N = 3
M = 3
K = 3
Edges = [[1, 2], [2, 3], [3, 1]]
print(max_edges_to_remove(N, M, K, Edges))
