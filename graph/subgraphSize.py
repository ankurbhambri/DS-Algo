'''
Similar to connected component technique but in this we are just calculating size 
for all nodes and saving it in a dictionary.
'''
def subGraphSize(n, graph):
    # Vertices stating from 1
    adj = {i: [] for i in range(1, n + 1)}
    size = {i: 0 for i in range(1, n + 1)}  # size of graph from a node
    for u, v in graph:
        adj[u].append(v)
        adj[v].append(u)
    visit = set()

    def dfs(node):
        sm = 0
        visit.add(node)
        for ch in adj[node]:
            if ch not in visit:
                sm += dfs(ch)
        size[node] = sm + 1
        return size[node]

    return dfs(1), size


graph = [[1, 2], [2, 4], [2, 5], [2, 6], [1, 3], [3, 7], [1, 8]]
n = 8

print(subGraphSize(n, graph))
