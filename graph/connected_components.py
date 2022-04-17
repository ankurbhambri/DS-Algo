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

# Count nos of Connected Components in an Undirected Graph using UNION and FIND algo


def countComponent(n, edges):

    adj = [i for i in range(n)]  # everyone iteself parent

    def find(node):
        if adj[node] != node:
            adj[node] = find(adj[node])
        return adj[node]

    def union(node1, node2):
        p1, p2 = find(node1), find(node2)
        if p1 != p2:
            adj[node2] = adj[
                node1
            ]  # if both have different parent then node1 parent will be node2 parent
            return 1
        return 0

    res = n
    for n1, n2 in edges:
        res -= union(n1, n2)
    return res


n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(countComponent(n, edges))
