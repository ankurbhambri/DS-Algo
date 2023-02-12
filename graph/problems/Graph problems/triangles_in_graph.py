'''
Given n nodes and edges of an undirected graph. How many triangles are there in this graph? Triangle is a cycle of length 3.

Example 1:

Input: n = 6, edges = [[0,1], [3,0], [0,2], [3,2], [1,2], [4,0], [3,4], [3,5], [4,5], [1,5], [1,3]]
Output: 7
'''

from collections import defaultdict


def count_triangles(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    count = 0
    for u in range(n):
        for v in graph[u]:
            for w in graph[v]:
                if u in graph[w]:
                    count += 1
    return count // 6


n = 6
edges = [
    [0, 1],
    [3, 0],
    [0, 2],
    [3, 2],
    [1, 2],
    [4, 0],
    [3, 4],
    [3, 5],
    [4, 5],
    [1, 5],
    [1, 3],
]
print(count_triangles(n, edges))  # Output: 7

n = 4
edges = [[0, 1], [1, 2], [2, 3], [3, 0]]
print(count_triangles(n, edges))  # Output: 1

n = 4
edges = [[0, 1], [1, 2], [2, 3]]
print(count_triangles(n, edges))  # Output: 0

n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]
print(count_triangles(n, edges))  # Output: 2
