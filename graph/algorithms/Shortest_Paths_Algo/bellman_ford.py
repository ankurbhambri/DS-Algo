"""Shortest path algorithm works with negative weights but when the cycle found it fials
It runs algorithm V - 1 times relations of vertices using edges weights - o(n^2)"""


# Function to find the shortest path between a given source node and all other nodes in a graph using Bellman-Ford algorithm
def bellman_ford(graph, source):
    # Step 1: Initialize distance of all nodes as infinity except the source node, which has distance 0
    V = len(graph)
    distance = {node: float("inf") for node in graph}
    distance[source] = 0

    # Step 2: Relax edges repeatedly |V - 1| times
    for _ in range(V - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distance[node] + weight < distance[neighbor]:
                    distance[neighbor] = distance[node] + weight

    # Even after relaxation we found some improvement that means -ve weight and cycle.
    # Step 3: Check for negative-weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distance[node] + weight < distance[neighbor]:
                print("Graph contains negative-weight cycle")
                return {}

    # Step 4: Return the shortest distance between the source node and all other nodes
    return distance
