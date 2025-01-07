"""Minimum Cost Spanning Tree using min heap O(nlogn)"""


class UnionFind:
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
            return False

        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1

        self.parent[p2] = p1
        self.rank[p1] += self.rank[p2]

        return True


# We have to select minimum cost edges which must not be part of same parent.
def kruskal_mst(edges, n):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    # Initialize Union-Find
    uf = UnionFind(n)
    mst_weight = 0

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):  # No cycle
            uf.union(u, v)
            mst_weight += weight

    return mst_weight


# u, v weight
edges = [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]
n = 5
print(kruskal_mst(edges, n))  # Output: 16


# https://leetcode.com/problems/connecting-cities-with-minimum-cost/


def minimumCost(n, connections):

    uf = UnionFind(n + 1)

    connections.sort(key=lambda x: x[2])

    mst_cost = 0

    # Process edges in ascending order of cost
    for city1, city2, cost in connections:
        if uf.union(city1, city2):
            mst_cost += cost
            n -= 1
            # If we have used n-1 edges, the MST is complete
            if n == 1:
                return mst_cost

    # If we didn't use N-1 edges, the graph is disconnected
    return -1


print(minimumCost(3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]))  # Output: 6
print(minimumCost(4, [[1, 2, 3], [3, 4, 4]]))  # Output: -1


# https://leetcode.com/problems/min-cost-to-connect-all-points/


def minCostConnectPoints(points):

    n = len(points)
    res = 0

    uf = UnionFind(n)

    edges = []

    # Create all edges with Manhattan distance
    for i in range(n):
        for j in range(i + 1, n):
            distance = abs(points[i][0] - points[j][0]) + abs(
                points[i][1] - points[j][1]
            )
            edges.append((distance, i, j))

    # Sort edges by weight
    edges.sort()

    for dist, i, j in edges:
        if uf.union(i, j):
            res += dist
            n -= 1
            # If we have used N-1 edges, the MST is complete
            if n == 1:  # All points are connected
                break

    return res


print(minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))  # Output: 20
print(minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))  # Output: 18
