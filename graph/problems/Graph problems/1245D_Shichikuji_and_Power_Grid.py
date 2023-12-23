# https://codeforces.com/contest/1245/problem/D


def first():
    #  Manhattan distance between two cities
    def manhattan_distance(city1, city2):
        return abs(city1[0] - city2[0]) + abs(city1[1] - city2[1])

    # Input
    n = int(input())
    cities = [list(map(int, input().split())) for _ in range(n)]
    costs_stations = list(map(int, input().split()))
    costs_connections = list(map(int, input().split()))

    # Initialize variables
    total_cost = 0
    power_stations = []
    connections = []

    # Find the minimum cost solution
    for i in range(n):
        min_cost = float("inf")
        station_idx = -1

        # Check the cost of building a station in each city
        for j in range(n):
            if i != j:
                cost = manhattan_distance(cities[i], cities[j]) * (
                    costs_connections[i] + costs_connections[j]
                )
                if cost < min_cost:
                    min_cost = cost
                    station_idx = j

        # Compare the cost of building a station vs making a connection
        if min_cost < costs_stations[i]:
            connections.append((i + 1, station_idx + 1))
            total_cost += min_cost
        else:
            power_stations.append(i + 1)
            total_cost += costs_stations[i]

    print(total_cost)  # the minimum amount of yen needed
    # print an integer v — the number of power stations to be built.
    print(len(power_stations))
    # v space-separated integers, denoting the indices of cities in which a power station will be built
    print(*power_stations)
    # After that, print an integer e — the number of connections to be made.
    print(len(connections))
    # print e pairs of integers a and b
    for connection in connections:
        print(*connection)


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, vertex1, vertex2):
        parent_vertex1 = self.find(vertex1)
        parent_vertex2 = self.find(vertex2)

        if parent_vertex1 != parent_vertex2:
            if self.size[parent_vertex1] < self.size[parent_vertex2]:
                parent_vertex1, parent_vertex2 = parent_vertex2, parent_vertex1
            self.parent[parent_vertex2] = parent_vertex1
            self.size[parent_vertex1] += self.size[parent_vertex2]


class Solution:
    def solve(self):
        n = int(input())
        coordinates = [(-1, -1)] * (n + 1)
        cost_power = [-1] * (n + 1)
        cost_wire = [-1] * (n + 1)

        for i in range(1, n + 1):
            x, y = map(int, input().split())
            coordinates[i] = (x, y)

        cost_power[1:] = map(int, input().split())
        cost_wire[1:] = map(int, input().split())

        edges = [(cost_power[i], 0, i) for i in range(1, n + 1)]
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                dis = abs(coordinates[j][0] - coordinates[i][0]) + abs(
                    coordinates[j][1] - coordinates[i][1]
                )
                cost = dis * (cost_wire[i] + cost_wire[j])
                edges.append((cost, i, j))

        edges.sort()
        total = 0
        uf = UnionFind(n)

        power_stations = []
        wires = []
        for edge in edges:
            wt, v1, v2 = edge
            if uf.find(v2) == uf.find(v1):
                continue
            uf.union(v1, v2)
            total += wt
            if v1 == 0 or v2 == 0:
                power_stations.append(max(v1, v2))
            else:
                wires.append((v1, v2))

        print(total)
        print(len(power_stations))
        print(*power_stations)
        print(len(wires))
        for w in wires:
            print(*w)


if __name__ == "__main__":
    first()
    # Solution().solve()
