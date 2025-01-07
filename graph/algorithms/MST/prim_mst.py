""" 
Minimum Spanning Tree MST select min cost vertex but no cycle will be formed.

We have to select minimum cost edge but make sure next vertex must me connected to selected one.

The time complexity of Prim's algorithm for finding the Minimum Spanning Tree 
(MST) of an undirected weighted graph is O(E log V), where E is the number of 
edges and V is the number of vertices in the graph.
"""

import heapq


def prim_mst(graph):
    # Number of vertices
    n = len(graph)

    # Priority Queue to pick the smallest edge
    pq = []

    # Start with node 0
    visited = [False] * n
    mst_weight = 0

    # Add all edges from the start node (node 0)
    for neighbor, weight in graph[0]:
        heapq.heappush(pq, (weight, neighbor))

    visited[0] = True  # Mark node 0 as visited

    while pq:
        weight, node = heapq.heappop(pq)  # Pick the smallest edge

        if visited[node]:
            continue  # Ignore if already visited

        # Add the weight to the MST
        mst_weight += weight
        visited[node] = True

        # Add all edges from this node to the PQ
        for neighbor, edge_weight in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(pq, (edge_weight, neighbor))

    return mst_weight


# Adjacency list representation of the graph
# Example graph with 5 nodes
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)],
}

# Convert the dictionary into a list for Prim's algorithm
adj_list = [[] for _ in range(len(graph))]
for u, edges in graph.items():
    for v, weight in edges:
        adj_list[u].append((v, weight))

# Call the function
mst_weight = prim_mst(adj_list)
print(f"The weight of the Minimum Spanning Tree is: {mst_weight}")
