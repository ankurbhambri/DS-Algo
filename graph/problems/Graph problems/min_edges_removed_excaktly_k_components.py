# https://www.geeksforgeeks.org/maximum-number-of-edges-to-be-removed-to-contain-exactly-k-connected-components-in-the-graph/


def max_edges_to_remove(N, M, K, Edges):
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

    if c <= K:
        return (
            M - N + K
        )  # N is the number f nodes, M is the number of edges and K is the required number of connected components.

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
