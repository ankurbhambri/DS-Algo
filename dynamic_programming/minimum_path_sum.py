# https://leetcode.com/problems/minimum-path-sum/


# memoization
# TC O(M * N)
# Space O(M * N) + Stack space
def minSumPath(matrix):

    m, n = len(grid), len(grid[0])
    memo = [[-1 for _ in range(n)] for _ in range(m)]

    def helper(i, j):

        if memo[i][j] != -1:
            return memo[i][j]

        if i == 0 and j == 0:
            memo[i][j] = grid[0][0]
            return memo[i][j]

        if i < 0 or j < 0:
            return float("inf")

        memo[i][j] = grid[i][j] + min(helper(i - 1, j), helper(i, j - 1))
        return memo[i][j]

    helper(m - 1, n - 1)
    return memo[m - 1][n - 1]


# tabulation
# TC O(M * N)
# Space O(M * N)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    up = grid[i][j] + (float("inf") if i == 0 else dp[i - 1][j])
                    left = grid[i][j] + (float("inf") if j == 0 else dp[i][j - 1])
                    dp[i][j] = min(up, left)

        return dp[m - 1][n - 1]


# space optimization
# TC O(M * N)
# Space O(N)
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
