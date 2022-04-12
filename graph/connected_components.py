def func(graph, all_nodes, find_nodes):

    adj = {i: [] for i in all_nodes}

    for u, v in graph:
        adj[u].append(v)
        adj[v].append(u)
    visit = set()

    def dfs(nv):
        sm = 0
        visit.add(nv)
        for ch in adj[nv]:
            if ch not in visit:
                sm += dfs(ch)
        return sm + 1

    res = []
    for n in find_nodes:
        res.append((n, dfs(n)))

    return res


graph = [
    ['A', 'B'],
    ['A', 'C'],
    ['A', 'D'],
    ['D', 'E'],
    ['B', 'E'],
    ['F', 'H'],
    ['F', 'G'],
    ['I', 'J'],
]
all_nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'H']

find_nodes = ['A', 'F', 'I', 'K']

print(func(graph, all_nodes, find_nodes))
