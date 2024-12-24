# https://www.geeksforgeeks.org/longest-path-undirected-tree/

# Given an undirected tree, we need to find the longest path of this tree where a path is defined as a sequence of nodes.


class Graph:

    def __init__(self, vertices):

        self.vertices = vertices
        self.adj = {i: [] for i in range(self.vertices)}

    def addEdge(self, u, v):

        self.adj[u].append(v)
        self.adj[v].append(u)

    def BFS(self, u):

        visit = set()
        dist = [0] * self.vertices
        dist[u] = 0
        q = [u]

        while q:
            node = q.pop(0)
            for nei in self.adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    dist[nei] = dist[node] + 1
                    q.append(nei)

        maxDist = 0

        for i in range(self.vertices):
            if dist[i] > maxDist:
                maxDist = dist[i]
                node = i

        return node, maxDist

    def LongestPathLength(self):

        node, _ = self.BFS(0)

        node_2, LongDis = self.BFS(node)

        return f'Longest path is from", {node}, "to", {node_2}, "of length", {LongDis}'


G = Graph(10)
G.addEdge(0, 1)
G.addEdge(1, 2)
G.addEdge(2, 3)
G.addEdge(2, 9)
G.addEdge(2, 4)
G.addEdge(4, 5)
G.addEdge(1, 6)
G.addEdge(6, 7)
G.addEdge(6, 8)

print(G.LongestPathLength())


# Similar - Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.
# The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

# https://leetcode.ca/all/1245.html

from collections import defaultdict


def tree_diameter(edges):

    if not edges:
        return 0

    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(node, visited):

        visited.add(node)
        max_distance, farthest_node = 0, node

        for neighbor in adj[node]:
            if neighbor not in visited:
                distance, far_node = dfs(neighbor, visited)
                if distance + 1 > max_distance:
                    max_distance = distance + 1
                    farthest_node = far_node
        return max_distance, farthest_node

    # First DFS to find the farthest node from an arbitrary node (e.g., 0)
    _, farthest_node = dfs(0, set())

    # Second DFS from the farthest node found
    max_distance, _ = dfs(farthest_node, set())

    return max_distance


edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]
print(tree_diameter(edges))  # Output: 4

edges = [[0, 1], [0, 2]]
print(tree_diameter(edges))  # Output: 2

edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [1, 4],
    [4, 5],
    [4, 6],
    [6, 7],
    [6, 8],
    [8, 9],
    [8, 10],
]
print(tree_diameter(edges))  # Output: 6

edges = [[0, 1], [1, 2], [2, 3], [2, 9], [2, 4], [4, 5], [1, 6], [6, 7], [6, 8]]
print(tree_diameter(edges))  # Output: 5
