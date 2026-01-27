'''

How it Works: To find the shortest path in unweighted graphs - BFS

BFS explores a graph in "waves." This is why it's perfect for finding the shortest path in unweighted graphs:

    Level 0: The root (distance 0).
    Level 1: All immediate neighbors of the root (distance 1).
    Level 2: All neighbors of Level 1 nodes that haven't been visited yet (distance 2).


Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges. We visit every node and every edge once.
Space Complexity: O(V) to store the distances dictionary and the queue.

Note: If your graph had weights (e.g., the edge from A to B costs 5), BFS would no longer guarantee the shortest path. In that case, we want to look into Dijkstra's Algorithm.

'''

from collections import deque

def bfs_shortest_path(graph, root):

    # distance dict
    distances = {node: float("inf") for node in graph}
    distances[root] = 0

    queue = deque([root])

    while queue:

        current_node = queue.popleft()

        for neighbor in graph[current_node]:

            if distances[neighbor] == float("inf"):

                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)

    return distances


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
print(bfs_shortest_path(graph, "A"))