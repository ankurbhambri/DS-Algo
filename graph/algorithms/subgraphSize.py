"""
Similar to connected component technique but in this we are just calculating subtree_size 
for all nodes and saving it in a dictionary.

Similar problems:

- https://leetcode.com/problems/maximum-number-of-k-divisible-components/
- https://leetcode.com/problems/create-components-with-same-value/

"""

from collections import defaultdict


def subGraphSize(edges):

    # Total number of nodes
    n = len(edges) + 1

    adj = defaultdict(list)

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visit = set()
    subtree_size = [0] * n  # Array to store subtree sizes

    def dfs(node):

        sm = 1
        visit.add(node)

        for nei in adj[node]:

            if nei not in visit:
                sm += dfs(nei)

        subtree_size[node] = sm
        return sm

    dfs(0)
    return subtree_size


edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [1, 4],
    [2, 5],
    [2, 6],
    [3, 7],
    [3, 8],
    [4, 9],
    [4, 10],
]
print(subGraphSize(edges))  # Output: [11, 7, 3, 3, 3, 1, 1, 1, 1, 1, 1]

edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [1, 4],
    [2, 5],
    [2, 6],
    [3, 7],
    [3, 8],
    [4, 9],
    [4, 10],
    [5, 11],
    [5, 12],
]
print(subGraphSize(edges))  # Output: [13, 7, 5, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1]

edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [1, 4],
    [2, 5],
    [2, 6],
    [3, 7],
    [3, 8],
    [4, 9],
    [4, 10],
    [5, 11],
    [5, 12],
    [6, 13],
    [6, 14],
]
print(subGraphSize(edges))  # Output: [15, 7, 7, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1]

edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [1, 4],
    [2, 5],
    [2, 6],
    [3, 7],
    [3, 8],
    [4, 9],
    [4, 10],
    [5, 11],
    [5, 12],
    [6, 13],
    [6, 14],
    [7, 15],
    [7, 16],
]
print(
    subGraphSize(edges)
)  # Output: [17, 9, 7, 5, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]

edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [1, 4],
    [2, 5],
    [2, 6],
    [3, 7],
    [3, 8],
    [4, 9],
    [4, 10],
    [5, 11],
    [5, 12],
    [6, 13],
    [6, 14],
    [7, 15],
    [7, 16],
    [8, 17],
    [8, 18],
]
print(
    subGraphSize(edges)
)  # Output: [19, 11, 7, 7, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
