# https://codeforces.com/contest/1245/problem/D

# manhatan_distance's formula - |x1 - x2| + |y1 - y2|

import heapq

# Prim’s Algorithm


def prim_algorithm(n, coordinates, power_costs, connection_costs):

    visited = [False] * (n + 1)  # Visited nodes
    pq = []  # Priority queue for edges (cost, u, v)
    total_cost = 0
    power_stations = []
    connections = []

    # Add edges from dummy node (0) to all cities
    for i in range(1, n + 1):
        heapq.heappush(pq, (power_costs[i - 1], 0, i))

    # Process the priority queue
    while pq:
        cost, u, v = heapq.heappop(pq)
        if visited[v]:
            continue
        visited[v] = True
        total_cost += cost

        if u == 0:
            power_stations.append(v)
        else:
            connections.append((u, v))

        # Add edges from the current city to all unvisited cities
        for j in range(1, n + 1):
            if not visited[j]:
                connection_cost = (
                    connection_costs[v - 1] + connection_costs[j - 1]
                ) * (
                    abs(coordinates[v - 1][0] - coordinates[j - 1][0])
                    + abs(coordinates[v - 1][1] - coordinates[j - 1][1])
                )
                heapq.heappush(pq, (connection_cost, v, j))

    return total_cost, power_stations, connections


# Example input

n = 3
coordinates = [(2, 3), (1, 1), (3, 2)]
power_costs = [3, 2, 3]
connection_costs = [3, 2, 3]

total_cost, power_stations, connections = prim_algorithm(
    n, coordinates, power_costs, connection_costs
)

print("Total Cost:", total_cost)
print("Nos of Power Stations:", len(power_stations))
print("Power Stations:", power_stations)
print("Nos of Connections:", len(connections))
print("Connections:", connections)


n = 3
coordinates = [(2, 1), (1, 2), (3, 3)]
power_costs = [23, 2, 23]
connection_costs = [3, 2, 3]

total_cost, power_stations, connections = prim_algorithm(
    n, coordinates, power_costs, connection_costs
)

print("Total Cost:", total_cost)
print("Nos of Power Stations:", len(power_stations))
print("Power Stations:", power_stations)
print("Nos of Connections:", len(connections))
print("Connections:", connections)

n = 1
coordinates = [(1, 1)]
power_costs = [1]
connection_costs = [1]

total_cost, power_stations, connections = prim_algorithm(
    n, coordinates, power_costs, connection_costs
)

print("Total Cost:", total_cost)
print("Nos of Power Stations:", len(power_stations))
print("Power Stations:", power_stations)
print("Nos of Connections:", len(connections))
print("Connections:", connections)


print(
    "##################################################################################"
)


# Union-Find (Kruskal’s Algorithm)
def kruskal_algorithm(n, coordinates, power_costs, connection_costs):

    edges = []
    total_cost = 0
    power_stations = []
    connections = []

    # Add edges from the dummy node (0) to all cities
    for i in range(1, n + 1):
        edges.append((power_costs[i - 1], 0, i))

    # Add edges between every pair of cities
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):

            # manhatan_distance's formula - |x1 - x2| + |y1 - y2|
            manhatan_distance = abs(
                coordinates[i - 1][0] - coordinates[j - 1][0]
            ) + abs(coordinates[i - 1][1] - coordinates[j - 1][1])

            cost = (
                connection_costs[i - 1] + connection_costs[j - 1]
            ) * manhatan_distance

            edges.append((cost, i, j))

    # Sort edges by weight
    # edges.sort()
    heapq.heapify(edges)

    # Initialize Union-Find structure
    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(node1, node2):

        p1 = find(parent, node1)
        p2 = find(parent, node2)

        # If both nodes parent are same then union is not possible
        if p1 == p2:
            # print("Same parent")
            return

        if rank[p1] < rank[p2]:
            p1, p2 = p2, p1

        parent[p2] = p1
        rank[p1] += rank[p2]
        return

    # Process edges
    for cost, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(u, v)
            total_cost += cost
            if u == 0:
                power_stations.append(v)
            else:
                connections.append((u, v))

    return total_cost, power_stations, connections


# Test cases for both functions

n = 3
coordinates = [(2, 3), (1, 1), (3, 2)]
power_costs = [3, 2, 3]
connection_costs = [3, 2, 3]

total_cost, power_stations, connections = kruskal_algorithm(
    n, coordinates, power_costs, connection_costs
)

print("Total Cost:", total_cost)
print("Nos of Power Stations:", len(power_stations))
print("Power Stations:", power_stations)
print("Nos of Connections:", len(connections))
print("Connections:", connections)


n = 3
coordinates = [(2, 1), (1, 2), (3, 3)]
power_costs = [23, 2, 23]
connection_costs = [3, 2, 3]

total_cost, power_stations, connections = kruskal_algorithm(
    n, coordinates, power_costs, connection_costs
)

print("Total Cost:", total_cost)
print("Nos of Power Stations:", len(power_stations))
print("Power Stations:", power_stations)
print("Nos of Connections:", len(connections))
print("Connections:", connections)


n = 1
coordinates = [(1, 1)]
power_costs = [1]
connection_costs = [1]

total_cost, power_stations, connections = kruskal_algorithm(
    n, coordinates, power_costs, connection_costs
)

print("Total Cost:", total_cost)
print("Nos of Power Stations:", len(power_stations))
print("Power Stations:", power_stations)
print("Nos of Connections:", len(connections))
print("Connections:", connections)
