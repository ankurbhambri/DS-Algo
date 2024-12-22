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
