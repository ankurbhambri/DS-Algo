'''SSSP -> Single Source Shortest Path Using BFS and DFS'''

from collections import deque


def using_DFS(n, graph):

    dis = {i: 0 for i in range(n + 1)}
    adj = {i: [] for i in range(n + 1)}
    for u, v in graph:
        adj[u].append(v)
        adj[v].append(u)

    visit = set()

    def dfs(node):
        visit.add(node)
        for ch in adj[node]:
            if ch not in visit:
                dis[ch] = dis[node] + 1
                dfs(ch)

    dfs(1)
    return dis


def using_BFS(n, graph):

    dis = {i: 0 for i in range(n + 1)}
    adj = {i: [] for i in range(n + 1)}
    for u, v in graph:
        adj[u].append(v)
        adj[v].append(u)

    q = deque([1])
    visit = set([1])

    while q:
        node = q.popleft()
        for ch in adj[node]:
            if ch not in visit:
                visit.add(ch)
                q.append(ch)
                dis[ch] = dis[node] + 1
    return dis


graph = [[1, 2], [2, 4], [2, 5], [2, 6], [1, 3], [3, 7], [1, 8]]
n = 8
print(using_DFS(n, graph))
print(using_BFS(n, graph))