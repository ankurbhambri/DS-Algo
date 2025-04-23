# https://leetcode.com/problems/walls-and-gates/
from collections import deque

def wallsAndGates(grid):

    m, n = len(grid), len(grid[0])
    queue = deque()
    
    # treasure chests (0) in queue
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                queue.append((i, j))
    
    # bfs
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        
        # 4 neighbors
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check if new coordinates are valid and cell is INF
            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 2147483647:

                # distance = current cell ka distance + 1
                grid[new_x][new_y] = grid[x][y] + 1
                queue.append((new_x, new_y))


grid = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]

print(wallsAndGates(grid))
print(grid)  # [[3, -1, 0, 1], [2, 1, 2, -1], [1, -1, 3, -1], [0, -1, 4, 5] ]
