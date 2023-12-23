"""
A Bipartite graph is a graph whose vertices can be divided into two disjoint sets.
To check graph is Bipartite or not we represent vertices with color but condition is 
an adjacent node cannot be of same color is 0 then child must be 1.
"""


def bipartite(n, graph):
    adj = {i: [] for i in range(n + 1)}

    color = {i: 0 for i in range(n + 1)}

    for u, v in graph:
        adj[u].append(v)
        adj[v].append(u)

    visit = set()

    def dfs(node, c):
        visit.add(node)

        color[node] = c

        for child in adj[node]:
            if child not in visit:
                if not dfs(child, c ^ 1):
                    return False
            else:
                # False cndt
                if color[node] == color[child]:
                    return False

        return True

    return dfs(1, 0)


# graph = [[1, 2], [2, 4], [4, 3], [3, 1], [2, 5], [4, 5]]
# n = 5
graph = [[1, 2], [2, 3], [3, 6], [6, 5], [5, 4], [1, 4]]
n = 6
print(bipartite(n, graph))
