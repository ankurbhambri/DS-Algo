"""

Steps to Check if a Graph is Eulerian

Check Connectivity:
For an undirected graph, use a graph traversal method (DFS or BFS) to ensure all vertices with at least one edge are part of a single connected component.
For a directed graph, ensure that for every vertex, the total number of incoming edges equals the total number of outgoing edges.

Check Degree of Vertices:
For each vertex in the graph, count the degree (number of edges connected to it).

For an undirected graph:
- If all vertices have even degrees, it's Eulerian (has an Eulerian Circuit).
- If exactly two vertices have odd degrees, it has an Eulerian Path.
- Otherwise, it’s not Eulerian.

For a directed graph:
- If in-degree = out-degree for every vertex, it has an Eulerian Circuit.
- If exactly two vertices have mismatched in-degree and out-degree (one has in-degree - out-degree = 1, and the other has out-degree - in-degree = 1), it has an Eulerian Path.

"""

from collections import defaultdict

# Undirected Graph


def is_connected(graph, start):
    visited = set()

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

    dfs(start)
    # Check if all nodes with edges are visited
    return all(node in visited for node in graph if graph[node])


def is_eulerian(graph):
    # Count vertices with odd degree
    odd_degree_count = 0
    for node, edges in graph.items():
        if len(edges) % 2 != 0:
            odd_degree_count += 1

    # Check connectivity and degree conditions
    if not is_connected(graph, next(iter(graph))):  # Check connectivity
        return "Not Eulerian"
    if odd_degree_count == 0:
        return "Eulerian Circuit"
    elif odd_degree_count == 2:
        return "Eulerian Path"
    else:
        return "Not Eulerian"


# Example Graph as Adjacency List
graph = {"A": ["B", "C", "D"], "B": ["A", "C"], "C": ["A", "B"], "D": ["A"]}

print(is_eulerian(graph))  # Output: Eulerian Path


# Directed Graph

"""
Steps to Check if a Directed Graph is Eulerian

Check Strong Connectivity:
A directed graph is strongly connected if there is a directed path from any vertex to every other vertex. Use Depth-First Search (DFS) or any similar algorithm to verify this.
If the graph is not strongly connected, it is not Eulerian.

Check Degree Conditions:
For an Eulerian Circuit:
- In-degree = Out-degree for all vertices.

For an Eulerian Path:
- Exactly one vertex should have out-degree - in-degree = 1 (starting point of the path).
- Exactly one vertex should have in-degree - out-degree = 1 (ending point of the path).
- All other vertices should have in-degree = out-degree.
"""


# Hierholzer Alogorithm to find Eulerian Path/Circuit
def find_eulerian_path(graph):
    # Count in-degrees and out-degrees
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    for node, neighbors in graph.items():
        out_degree[node] += len(neighbors)
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    start_node = None
    end_node = None

    for node in set(in_degree.keys()).union(set(out_degree.keys())):
        if out_degree[node] - in_degree[node] == 1:
            if start_node is not None:
                return "Not Eulerian"
            start_node = node
        elif in_degree[node] - out_degree[node] == 1:
            if end_node is not None:
                return "Not Eulerian"
            end_node = node
        elif in_degree[node] != out_degree[node]:
            return "Not Eulerian"

    if start_node is None:  # Eulerian Circuit
        start_node = next(iter(graph))

    # Hierholzer's Algorithm to find the path/circuit
    stack = [start_node]
    path = []

    while stack:
        current = stack[-1]
        if graph[current]:
            next_node = graph[current].pop()
            stack.append(next_node)
        else:
            path.append(stack.pop())

    return path[::-1]  # Reverse the path to get the correct order

print(find_eulerian_path(graph))  # Output: ['A', 'D', 'A', 'C', 'B', 'A']
print(find_eulerian_path({"A": ["B"], "B": ["C"], "C": ["A"]}))  # Output: ['A', 'B', 'C', 'A']