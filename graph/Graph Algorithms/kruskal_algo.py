'''Minimum Cost Spanning Tree using min heap O(nlogn)'''
import heapq

# We have to select minimum cost edge whether it's connected to selected one or not.


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
    # rather than sorting we can use min heap aka priority queue Time complexity will be (O(nlogn)) else O(n^2logn)
    # heapq.heapify(graph)
    graph = sorted(graph, key=lambda i: i[2])
    adj = [i for i in range(n + 1)]
    for u, v, _ in graph:  # all nodes in graph in sorted order by weight
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