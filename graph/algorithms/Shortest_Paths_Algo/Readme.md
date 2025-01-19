| Use Case                        | Algorithm               | Notes                                      | Description                                                                 |
|---------------------------------|-------------------------|--------------------------------------------|-----------------------------------------------------------------------------|
| Unweighted Graphs               | BFS                     | Shortest path by edges.                    | Breadth-First Search finds the shortest path in terms of the number of edges. |
| Binary Weighted Graphs          | 0-1 BFS                 | Shortest path with weights 0 or 1.         | A variation of BFS for graphs with edge weights of 0 or 1.                   |
| Arbitrary Positive Weights      | Dijkstra's Algorithm    | Shortest path efficiently.                 | Efficiently finds the shortest path in graphs with positive weights.         |
| Negative Weights                | Bellman-Ford Algorithm  | Shortest path with negative weights.       | Handles graphs with negative weight edges, but slower than Dijkstra's.       |
| All-Pairs Shortest Path         | Floyd-Warshall Algorithm| Dense graphs or multiple paths needed.     | Computes shortest paths between all pairs of vertices.                       |
| Minimum Spanning Tree (Sparse)  | Kruskal’s Algorithm     | Edge list, disjoint-set.                   | Finds the minimum spanning tree using a greedy approach.                     |
| Minimum Spanning Tree (Dense)   | Prim’s Algorithm        | Adjacency list/matrix.                     | Another greedy algorithm for finding the minimum spanning tree.              |
| Strongly Connected Components   | Tarjan's Algorithm      | Directed graphs.                           | Finds all strongly connected components in a directed graph.                 |
| Topological Sorting in DAG      | Kahn’s Algorithm        | Dependency graphs.                         | Performs topological sorting on directed acyclic graphs.                     |
| Pathfinding with Heuristic      | A* Search               | Grids or maps with heuristic function.     | Uses heuristics to find the shortest path, often used in pathfinding on maps.|
