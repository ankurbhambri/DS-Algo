# https://leetcode.com/problems/number-of-islands/description/

def numIslands(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    islands = 0
    
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
