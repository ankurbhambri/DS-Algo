# https://leetcode.com/problems/island-perimeter/


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):

            # If out of bounds or water, return 1 (found a perimeter edge).
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1

            if grid[i][j] == -1: # to mark visited cells
                return 0

            grid[i][j] = -1

            perim = dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i - 1, j)

            return perim

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i, j)

        return 0


print(Solution().islandPerimeter(
    [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
))  # output: 16