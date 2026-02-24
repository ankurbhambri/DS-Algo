# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid):

        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        # Fill first row
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # Fill first column
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, m):

            for j in range(1, n):

                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


print(Solution().minPathSum([[1, 2], [3, 4]]))  # Output: 10
print(Solution().minPathSum([[1, 2, 3], [4, 5, 6]]))  # Output: 12
print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # Output: 7
print(Solution().minPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: 21
