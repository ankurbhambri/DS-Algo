'''SSSP -> Single Source Shortest Path Using BFS and DFS
Finding the shortest paths between a given vertex v and all other vertices in the graph.
'''


def using_DFS(n, graph):

    # distance list to get distance from parent node
    dis = {i: 0 for i in range(1, n + 1)}  

    # adjacency list
    adj = {i: [] for i in range(1, n + 1)}

    for u, v in graph:
        adj[u].append(v)
        adj[v].append(u)

    visit = set()

    def dfs(node):
        visit.add(node)
        for ch in adj[node]:
            if ch not in visit:
                dis[ch] = 1 + dis[node]
                dfs(ch)

    dfs(1) # start node
    return dis


def using_BFS(n, graph):

    dis = {i: 0 for i in range(1, n + 1)}
    adj = {i: [] for i in range(1, n + 1)}
    for u, v in graph:
        adj[u].append(v)
        adj[v].append(u)

    q = []
    q.append(1)
    visit = set([1])

    while q:
        node = q.pop(0)
        for ch in adj[node]:
            if ch not in visit:
                visit.add(ch)
                q.append(ch)
                dis[ch] = 1 + dis[node]
    return dis


graph = [[1, 2], [2, 4], [2, 5], [2, 6], [1, 3], [3, 7], [1, 8]]
n = 8
print(using_DFS(n, graph))
print(using_BFS(n, graph))
