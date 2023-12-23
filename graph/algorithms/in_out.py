"""
To check whether node is a child of a node or not.
We calculate in and out time of every node.
Parent in time is always less than child in time but out time is greater than child.
"""


timer = 1


def in_out(n, graph):
    adj = {i: [] for i in range(1, n + 1)}
    for u, v in graph:
        adj[u].append(v)
        adj[v].append(u)

    in_t = {i: 0 for i in range(1, n + 1)}
    out_t = {i: 0 for i in range(1, n + 1)}
    visit = set()

    def dfs(node):
        global timer

        in_t[node] = timer
        timer += 1
        visit.add(node)

        for ch in adj[node]:
            if ch not in visit:
                dfs(ch)

        out_t[node] = timer
        timer += 1

    dfs(1)
    return in_t, out_t


graph = [[1, 2], [2, 4], [2, 5], [2, 6], [1, 3], [3, 7], [1, 8]]
n = 8
print(in_out(n, graph))
