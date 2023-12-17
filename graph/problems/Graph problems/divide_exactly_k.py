# https://www.geeksforgeeks.org/maximum-number-of-edges-to-be-removed-to-contain-exactly-k-connected-components-in-the-graph/

# Firstly, find the connected componenets like fo provinces logic
# Then, Nodes - (Edges + K) formaula to get min edges to removed for K component

def solve(N, M, graph, K):

    adj = {i: [] for i in range(1, N + 1)}
    visit = set()

    for u, v in graph:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(node):
        visit.add(node)
        for child in adj[node]:
            if child not in visit:
                dfs(child)
    c = 0
    for i in range(1, N + 1):
        if i not in visit:
            c += 1
            dfs(i)

    if c <= K:
        return M - N + K
    return -1


if __name__ == "__main__":

    N = 4
    M = 3
    K = 2

    Edges = [[1, 2], [2, 3], [3, 4]]
    print(solve(N, M, Edges, K))

    e = [[1, 2], [2, 3], [3, 1]]
    print(solve(3, 3, e, 3))
