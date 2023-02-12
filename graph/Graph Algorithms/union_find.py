# Clasical Way
class DisjointSet:
    def __init__(self, n, graph):
        self.n = n
        self.graph = graph
        # Root have negative value
        self.adj = {i: -1 for i in range(n)}

        for u, v in self.graph:
            self.adj[u] = v

    def find(self, node):

        if self.adj[node] < 0:
            return node
        return self.find(self.adj[node])

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        # If both nodes parent are same then union is not possible
        if p1 == p2:
            return False
        else:
            if self.adj[p1] == self.adj[p1]:
                self.adj[p1] += self.adj[p2]
                self.adj[p2] = p1
            # If p2 is gt than p1 then p1 is root for p2
            elif self.adj[p2] < self.adj[p1]:
                self.adj[p1] += self.adj[p2]
                self.adj[p2] = p1
            else:
                self.adj[p2] += self.adj[p1]
                self.adj[p1] = p2
        return True

    def peek(self):
        return self.adj


# Improved Code
class DisjointSet1:
    def __init__(self, n, graph):
        self.n = n
        self.graph = graph
        self.adj = [i for i in range(n)]

        for u, v in self.graph:
            self.union(u, v)

    def find(self, node):
        if self.adj[node] != node:
            self.adj[node] = self.find(self.adj[node])
        return self.adj[node]

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 != p2:
            self.adj[node2] = self.adj[node1]
            return True
        return False

    def peek(self):
        return self.adj


# obj = DisjointSet(7, [[0, 1], [1, 2], [2, 3], [4, 5]])
# obj.find(0)
# obj.find(4)
# print(obj.union(2, 4))
# print(obj.union(1, 5))
# print(obj.peek())


obj1 = DisjointSet1(7, [[0, 1], [1, 2], [2, 3], [4, 5]])
obj1.find(0)
obj1.find(4)
print(obj1.union(2, 4))
print(obj1.union(1, 5))
print(obj1.peek())
