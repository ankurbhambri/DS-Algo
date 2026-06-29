# https://leetcode.com/problems/number-of-provinces/

# TC: O(n^2)
# SC: O(n)

def solve(graph):
    n = len(graph)
    visit = set()

    def dfs(node):
        visit.add(node)
        for i in range(n):
            if graph[node][i] == 1 and i not in visit:
                dfs(i)

    res = 0
    for i in range(n):
        if i not in visit:
            res += 1
            dfs(i)

    return res

graph = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(solve(graph))


# Disjoint Set Union
# Time complexity: O(n)
# Space complexity: O(n)
class DisjointSet:
    def __init__(self, n):

        self.n = n
        # initially every noe rank is 0
        self.rank = [1] * n
        # initially every node is its own parent
        self.parent = list(range(n))

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):

        p1 = self.find(node1)
        p2 = self.find(node2)

        # If both nodes parent are same then union is not possible
        if p1 == p2:
            print("Same parent")
            return

        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1

        self.parent[p2] = p1
        self.rank[p1] += self.rank[p2]
        return

def solve(graph):
    n = len(graph)
    dsu = DisjointSet(n)

    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1:
                dsu.union(i, j)

    res = set()
    for i in range(n):
        res.add(dsu.find(i))

    return len(res)

graph = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(solve(graph))
