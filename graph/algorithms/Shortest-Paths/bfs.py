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


'''
Mooshak the mouse has been placed in a maze.There is a huge chunk of cheese somewhere in the maze.
The maze is represented as a two-dimensional array of integers, where 0 represents walls, 
1 represents paths where Mooshak can move, and 9 represents the huge chunk of cheese.Mooshak starts in the top-left corner at 0,0.

Write a method isPath of class Maze Path to determine if Mooshak can reach the huge chunk of cheese. 
The input to isPath consists of a two dimensional array grid for the maze matrix.

The method should return 1 if there is a path from Mooshak to the cheese, and 0 if not.
Mooshak is not allowed to leave the maze or climb on walls/

Example 8x8 maze where Mooshak can get the cheese.

1 0 1 1 1 0 0 1

1 0 0 0 1 1 1 1

1 0 0 0 0 0 0 0

1 0 1 0 9 0 1 1

1 1 1 0 1 0 0 1

1 0 1 0 1 1 0 1

1 0 0 0 0 1 0 1

1 1 1 1 1 1 1 1

'''

from collections import deque

class MazePath:
    def isPath(self, grid):
        # 1. Edge case: empty grid
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        # 2. Starting point: top-left corner (0,0)
        # Check if the start itself is a wall
        if grid[0][0] == 0:
            return 0
            
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        
        while queue:
            r, c = queue.popleft()
            
            # 3. Check if we found the cheese (9)
            if grid[r][c] == 9:
                return 1
            
            # 4. Explore neighbors (Up, Down, Left, Right)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                # Ensure neighbor is within bounds
                if 0 <= nr < rows and 0 <= nc < cols:
                    # Ensure neighbor is not a wall and not visited
                    if grid[nr][nc] != 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        
        # 5. If queue is empty and cheese not found
        return 0

# Example Usage:
# maze = MazePath()
# print(maze.isPath(grid_data))