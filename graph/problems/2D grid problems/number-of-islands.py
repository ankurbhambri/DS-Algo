# https://leetcode.com/problems/number-of-islands/description/

def numIslands(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    
    def dfs(i: int, j: int) -> None:

        # Base case: out of bounds or cell is water/visited
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
            return
        
        # Mark as visited by changing to '0'
        grid[i][j] = "0"
        
        # Recursively explore all 4 directions
        dfs(i-1, j)  # up
        dfs(i+1, j)  # down
        dfs(i, j-1)  # left
        dfs(i, j+1)  # right
    
    # Step 1: Iterate through each cell
    islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                islands += 1  # Found a new island
                dfs(i, j)    # Explore and mark the entire island
    
    return islands

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(grid))  # Output: 1


# VARIANT

'''

Given an m x n 2D binary grid grid which represents a map of '1's (land) and 'O's (water), 
return the area of each island. The output can be in any order.

An island is surrounded by water and is formed by connecting adjacent lands horizontally, vertically or diagonally. 

You may assume all eight edges of the grid are all surrounded by water.

'''

class Solution:
    def islandAreas(self, grid):
        if not grid:
            return []
        
        m, n = len(grid), len(grid[0])
        areas = []
        
        def dfs(i: int, j: int) -> int:

            # Base case: out of bounds or cell is water/visited
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return 0
            
            # Mark as visited by changing to '0'
            grid[i][j] = "0"
            
            area = 1  # Current cell
            
            # Recursively explore all 8 directions
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di != 0 or dj != 0:
                        area += dfs(i + di, j + dj)
            
            return area
        
        # Step 1: Iterate through each cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    area = dfs(i, j)  # Explore and calculate the area of the island
                    areas.append(area)

        return areas


print(Solution().islandAreas([
  ["1","1","0","0","0"],
  ["1","0","0","1","1"],
  ["0","0","0","0","0"],
  ["0","1","0","0","1"],
  ["1","1","0","1","1"]
]))  # Output: [3, 4, 1, 3]


############################################### Similar problems #######################################################

# https://leetcode.com/problems/max-area-of-island/


'''

    You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

    Return the size of the largest island in grid after applying this operation.

    An island is a 4-directionally connected group of 1s.

'''

class Solution:
    def maxAreaOfIsland(self, grid):

        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> None:

            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0

            # visited
            grid[i][j] = 0

            sm = 1
            sm += dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
            return sm

        max_size = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_size = max(max_size, dfs(i, j))
        
        return max_size

grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
print(Solution().maxAreaOfIsland(grid))  # Output: 6


# https://leetcode.com/problems/making-a-large-island/

class Solution:
    def largestIsland(self, grid):

        n = len(grid)
        island_sizes = {}
        island_id = 2  # 0 aur 1 pehle se grid mein hain, isliye 2 se start karenge
        
        # Step 1: DFS function island identify karne aur size nikalne ke liye
        def dfs(r, c, id):

            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0

            grid[r][c] = id
            size = 1

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                size += dfs(r + dr, c + dc, id)

            return size

        # Step 1 continued: Saare islands ko ID dena
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = dfs(r, c, island_id)
                    island_sizes[island_id] = size
                    island_id += 1
        
        # Agar puri grid 1 thi, toh answer n*n hoga
        max_area = max(island_sizes.values() or [0])
        
        # Step 2: Har '0' ko flip karke check karna
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:

                    seen_islands = set()

                    # Charo taraf ke neighbors check karo
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen_islands.add(grid[nr][nc])

                    # Current Area = 1 (flipped zero) + sum of unique neighbor islands
                    current_area = 1 + sum(island_sizes[iid] for iid in seen_islands)
                    max_area = max(max_area, current_area)
                    
        return max_area if max_area > 0 else n * n

print(Solution().largestIsland([[1,0],[0,1]]))  # Output: 3
print(Solution().largestIsland([[1,1],[1,0]]))  # Output: 4


# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/

def findMaxFish(grid):

    if not grid:
        return 0

    m, n = len(grid), len(grid[0])

    def dfs(i: int, j: int) -> None:

        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return 0

        sm = grid[i][j]

        grid[i][j] = 0

        sm += dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)

        return sm

    max_fish = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                max_fish = max(max_fish, dfs(i, j))

    return max_fish


grid = [
    [0,2,1,0],
    [4,0,0,3],
    [1,0,0,4],
    [0,3,2,0]
]
print(findMaxFish(grid))  # Output: 7


# https://leetcode.com/problems/count-sub-islands/description/


def countSubIslands(grid1, grid2):

    if not grid1 or not grid2:
        return 0
    
    m, n = len(grid1), len(grid1[0])
    count = 0
    
    def dfs(i: int, j: int) -> bool:

        # out of bounds
        if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
            return True
        
        # Mark current cell as visited
        grid2[i][j] = 0
        # Check if current cell is valid for sub-island
        is_valid = grid1[i][j] == 1
        
        # Check all 4 directions
        is_valid &= dfs(i-1, j)  # Up
        is_valid &= dfs(i+1, j)  # Down
        is_valid &= dfs(i, j-1)  # Left
        is_valid &= dfs(i, j+1)  # Right
        
        return is_valid
    
    # Traverse grid2
    for i in range(m):
        for j in range(n):
            if grid2[i][j] == 1:
                if dfs(i, j):  # if island have sub-island, then count
                    count += 1
    
    return count

grid1 = [
    [1,1,1,0,0],
    [0,1,1,1,1],
    [0,0,0,0,0],
    [1,0,0,0,0],
    [1,1,0,1,1]
]
grid2 = [
    [1,1,1,0,0],
    [0,0,1,1,1],
    [0,1,0,0,0],
    [1,0,1,1,0],
    [0,1,0,1,0]
]
print(countSubIslands(grid1, grid2))  # Output: 3


# https://leetcode.com/problems/number-of-distinct-islands/
# https://www.geeksforgeeks.org/problems/number-of-distinct-islands/1

class Solution:
    def numDistinctIslands(self, grid):

        rows, cols = len(grid), len(grid[0])
        unique_shapes = set()

        def dfs(r, c, direction, path):
            # Boundary check and early exit if cell is water
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = 0  # Mark cell as visited by setting to 0
                path.append(direction)

                # Explore all 4 directions
                dfs(r - 1, c, 'U', path)
                dfs(r + 1, c, 'D', path)
                dfs(r, c - 1, 'L', path)
                dfs(r, c + 1, 'R', path)

                path.append('B')  # Backtrack marker

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    path = []
                    dfs(r, c, 'S', path)
                    print(path)
                    unique_shapes.add(tuple(path))
        return len(unique_shapes)

print(Solution().numDistinctIslands([
    [1,1,0,0,0],
    [0,1,0,1,1],
    [0,0,0,0,0],
    [1,0,1,0,1],
    [1,1,0,0,0]
]))  # Output: 4


print(Solution().numDistinctIslands([
    [0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0],
    [1,1,0,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,0,1,0,0,1,0,1,0,0,1,0,1,1,1],
    [1,1,1,0,0,1,0,0,1,0,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0],
    [0,1,1,1,1,1,1,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,1,0,0,1,0,1,1,0,1,1,0,1,0,0,0,1],
    [0,0,0,0,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,0,0,0,0,1,1,1,1,1,0,1,0,0,0,1,1,0,0,0,0,0],
    [0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,1,0,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1,1,0],
    [1,1,0,0,1,0,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,0,1,1,1,1,1,0,1,0],
    [1,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,1,1,0,0,0,0,1],
    [1,1,0,0,1,0,0,0,1,0,1,0,1,0,0,1,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,1,1,0],
    [0,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0,1],
    [1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,1,0],
    [1,0,1,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,1,1,0,1,0,1,1,0,1,0,0,1,1,0,1,1,1,0,1,1,0,1],
    [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1],
    [1,1,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,0],
    [1,1,1,0,1,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1,0,0,0,0,1,1,1,1,1,0,0,1,0,1],
    [1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,1,0,1,0,1,1,1,0,0,0,1,0,1,1,0,1,0,1,0,1,1,0,0,1,0],
    [1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,1,0,0,1,0,1,0,1,1,1,1,1,0,0,1,0,0],
    [1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0],
    [1,0,0,1,1,1,1,0,0,1,1,0,0,0,1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1],
    [1,1,1,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,0,0,1],
    [1,0,0,1,1,1,1,0,0,1,0,1,1,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,1,1,1,1,0,1,0,1],
    [0,0,1,1,1,1,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,0,1,1,0,0],
    [0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,1,1,1,0,1,0,0,1,0,0,1,1,0,0,1,0,0,0,1],
    [0,0,0,1,0,1,0,1,1,1,1,0,1,0,1,1,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1],
    [1,0,1,1,1,1,1,0,1,1,0,0,1,1,1,0,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1],
    [0,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0],
    [0,0,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,0,0,0,0,0,0,1,0,1,0,0,0],
    [1,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,0,1,0,1,0,0,1,1,1,0,0,1,0],
    [1,0,0,1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,1,0,1,0,0,0,1,0,0,1,1,0,1,1,0],
    [1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0],
    [1,1,1,0,0,1,0,0,1,0,0,0,1,1,0,1,1,0,0,1,0,1,1,1,0,0,0,1,1,1,1,0,0,1,1,0,0,1,1,1],
    [1,1,0,1,1,1,1,1,0,1,1,0,0,1,0,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,0,1],
    [1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,0,1,0],
    [0,0,1,1,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,0,0,1,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,0],
    [1,0,0,0,0,1,0,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,1,0,0,0,1,0,1,0,0,1,1,1],
    [0,1,0,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,1,1,1,0,0,1],
    [1,1,0,0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,0],
    [0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,1,1,0,1,1,0,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,1,1,1],
    [0,1,1,1,1,0,1,1,1,1,1,0,0,0,1,0,1,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,0,0,0],
    [0,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1],
    [0,0,1,1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,0,1],
    [0,1,1,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,1,1],
    [0,0,0,1,0,1,1,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,0,1,1,0,1,1,0],
    [1,1,1,0,0,1,1,0,0,1,0,0,1,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,0,0,0,1,1,1,1],
    [1,1,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,1,0,1,1,0,0,0,1,1,0,1],
    [1,0,1,0,0,0,1,1,1,1,0,0,1,0,0,1,1,0,1,0,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,0,1,0],
    [1,1,1,0,1,1,1,0,0,1,1,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,1,1],
    [0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,1,1,1,1,0,0],
]))
