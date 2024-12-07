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
    for node in graph:
        if len(graph[node]) % 2 != 0:
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


def strongly_connected(graph, n):
    """
    Check if the graph is strongly connected using DFS
    """

    def dfs(node, visited, adj_list):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, adj_list)

    # First DFS on the graph
    visited = set()
    dfs(0, visited, graph)
    if len(visited) != n:
        return False

    # Transpose the graph
    transposed = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            transposed[v].append(u)

    # Second DFS on the transposed graph
    visited = set()
    dfs(0, visited, transposed)
    return len(visited) == n


def is_eulerian_directed(graph, n):
    """
    Determines if a directed graph is Eulerian
    """
    in_degree = [0] * n
    out_degree = [0] * n

    for u in graph:
        for v in graph[u]:
            out_degree[u] += 1
            in_degree[v] += 1

    # Check degree conditions
    start, end = 0, 0
    for i in range(n):
        if out_degree[i] - in_degree[i] == 1:
            start += 1
        elif in_degree[i] - out_degree[i] == 1:
            end += 1
        elif in_degree[i] != out_degree[i]:
            return "Not Eulerian"

    # Check connectivity
    if not strongly_connected(graph, n):
        return "Not Eulerian"

    # Determine if the graph has Eulerian Path or Circuit
    if start == 0 and end == 0:
        return "Eulerian Circuit"

    if start == 1 and end == 1:
        return "Eulerian Path"

    return "Not Eulerian"


# Example Directed Graph as Adjacency List
# Graph: 0 -> 1 -> 2 -> 0 and 1 -> 3
graph = {0: [1], 1: [2, 3], 2: [0], 3: []}

n = 4  # Number of vertices
print(is_eulerian_directed(graph, n))  # Output: Eulerian Path
