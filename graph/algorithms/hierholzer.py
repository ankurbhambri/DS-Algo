from collections import defaultdict

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


# Hierholzer Algorithm to find Eulerian Path/Circuit
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


graph = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"],
    "D": ["A"]
}
print(find_eulerian_path(graph))  # Output: ['D', 'A', 'B', 'C', 'A', 'B', 'C']
print(find_eulerian_path({"A": ["B"], "B": ["C"], "C": ["A"]}))  # Output: ['A', 'B', 'C', 'A']