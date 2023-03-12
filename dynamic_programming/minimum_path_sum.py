class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        prev = [0] * n

        for i in range(m):
            tmp = [0] * n
            for j in range(n):

                if i == 0 and j == 0:
                    tmp[j] = grid[i][j]

                else:
                    up = grid[i][j] + (float("inf") if i == 0 else prev[j])
                    left = grid[i][j] + (float("inf") if j == 0 else tmp[j - 1])

                    tmp[j] = min(up, left)

            prev = tmp

        return prev[-1]
