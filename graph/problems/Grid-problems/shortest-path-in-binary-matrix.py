from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        
        # Early exit if start or end is blocked
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        # 8 possible directions (including diagonals)
        directions = [
            (-1, -1), (-1, 0),
            (-1, 1), (0, -1),
            (0, 1), (1, -1),
            (1, 0), (1, 1)
        ]

        # BFS queue (x, y, path_length)
        queue = deque([(0, 0, 1)])
        visited = set((0, 0))
        
        while queue:
            x, y, length = queue.popleft()
            
            # If we reached the target
            if x == n - 1 and y == n - 1:
                return length
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if (0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited):
                    visited.add((nx, ny))
                    queue.append((nx, ny, length + 1))

        return -1

print(Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]]))  # Output: 2
print(Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))  # Output: 4
print(Solution().shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))  # Output: -1


# Variant: What if you had to return the actual shortest path itself? AKA the {row, col} coordinates.

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)

        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        directions = [
            (-1, -1), (-1, 0),
            (-1, 1), (0, -1),
            (0, 1), (1, -1),
            (1, 0), (1, 1)
        ]

        queue = deque([(0, 0, [(0, 0)])])  # (x, y, path)
        visited = set((0, 0))

        while queue:
            x, y, path = queue.popleft()

            if x == n - 1 and y == n - 1:
                return path

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited):
                    visited.add((nx, ny))
                    queue.append((nx, ny, path + [(nx, ny)]))

        return -1


# Variant: What if you had to return a single path, no need to return shortest path? Hint: use DFS.

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)

        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        directions = [
            (-1, -1), (-1, 0),
            (-1, 1), (0, -1),
            (0, 1), (1, -1),
            (1, 0), (1, 1)
        ]

        visited = set((0, 0))

        def dfs(x, y, path):

            if x == n - 1 and y == n - 1:
                return path

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited):

                    visited.add((nx, ny))
                    result = dfs(nx, ny, path + [(nx, ny)])

                    if result is not None:
                        return result

                    visited.remove((nx, ny))

            return None

        return dfs(0, 0, [(0, 0)]) or -1