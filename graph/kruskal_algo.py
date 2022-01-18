'''Minimum Cost Spanning Tree using min head O(nlogn)'''


def find(graph, node):
    if graph[node] != node:
        graph[node] = find(graph, graph[node])
    return graph[node]


def union(graph, node1, node2):
    p1, p2 = find(graph, node1), find(graph, node2)
    if p1 != p2:
        graph[node2] = graph[node1]
        return True
    return False


def kruskal(n, graph):
    res = []
    graph = sorted(graph, key=lambda i: i[2])
    adj = [i for i in range(n + 1)]
    for u, v, _ in graph:
        if union(adj, u, v):
            res.append((u, v))
    return res


dd = [
    [1, 2, 1],
    [1, 3, 3],
    [3, 6, 2],
    [2, 6, 4],
    [7, 5, 7],
    [4, 5, 5],
    [6, 5, 6],
    [3, 4, 1],
    [6, 7, 2],
]
print(kruskal(7, dd))
