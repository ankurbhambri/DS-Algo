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


if __name__ == "__main__":

    uf = DisjointSet(10)

    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(3, 4)

    uf.union(2, 4)  # not possible to union because same parent

    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(7, 8)
    uf.union(8, 9)

    print(uf.find(2))  # output: 0 -> connected to 1 but 1 itself parent is 0.
    print(uf.find(4))  # output: 0 -> connected to 3 -> 2 -> 1 -> 0.
    print(uf.find(9))  # output: 6 -> 8 -> 7 -> 6

    print(uf.find(1) == uf.find(2))  # True because their parents are same 0

    print(uf.find(4) == uf.find(9))  # False because their parents are different

    print(uf.parent, uf.rank)


# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

class DisjointSet:
    def __init__(self):
        self.parent = {}

    def find(self, x):

        if x not in self.parent:
            self.parent[x] = x

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def removeStones(self, stones):
        uf = DisjointSet()

        max_row = max(x for x, y in stones) + 1

        for x, y in stones:
            uf.union(x, y + max_row + 1)
        
        res = set()
        for x, y in stones:
            res.add(uf.find(x))
        
        return len(stones) - len(res)
