"""Minimum Cost Spanning Tree using min heap O(nlogn)"""

from union_find import DisjointSet

# We have to select minimum cost edges and edges must not be part of same parent.


def kruskal_algo(n, adj):
    res = []
    adj = sorted(adj, key=lambda i: i[2])
    obj = DisjointSet(n + 1)
    mst_cost = 0

    for u, v, weight in adj:
        if obj.find(u) != obj.find(v):
            mst_cost += weight
            res.append((u, v))
            obj.union(u, v)

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

print(kruskal_algo(7, dd))
