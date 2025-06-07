# https://leetcode.com/problems/unique-paths/

# memoization
# TC = O(M * N)
# SC = O(M * N) + Stack Space


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for i in range(n + 1)] for j in range(m + 1)]

        def helper(i, j):

            if i == 0 or j == 0:
                memo[i][j] = 1
                return 1

            if i < 0 or j < 0:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = helper(i - 1, j) + helper(i, j - 1)
            return memo[i][j]

        helper(m - 1, n - 1)
        return memo[m - 1][n - 1]


# tabulation
# TC = O(M * N)
# SC = O(M * N)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):

            for j in range(1, n):

                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]

print(Solution().uniquePaths(3, 7))
print(Solution().uniquePaths(3, 2))


# space optimization
# TC = O(M * N)
# SC = O(N)

class Solution:

    def uniquePaths(self, m, n):

        prev_row = [0] * n
        prev_row[0] = 1

        for i in range(m):

            tmp = [0] * n # current level row

            for j in range(n):

                if i == 0 and j == 0:
                    tmp[j] = 1

                else:
                    # checking top and left cells, top from prev_row, left from tmp[j - 1]
                    # then update the current cell in tmp
                    tmp[j] = prev_row[j] + tmp[j - 1]

            # update prev_row to be the current tmp row for the next iteration
            prev_row = tmp

        return prev_row[-1]

print(Solution().uniquePaths(3, 7))
print(Solution().uniquePaths(3, 2))


# https://leetcode.com/problems/unique-paths-ii/

'''
    Idea, here is botton up approach using DP.

    First we fill the first row and first column based on the obstacles.

    If the first cell is an obstacle, then return 0.

    If the first row or first column has an obstacle, then all cells after that in that row/column will be 0.

    If the cell is not an obstacle, then the number of unique paths to that cell is the sum of unique paths from the cell above it and the cell to the left of it.

    top: dp[i-1][j] (if not an obstacle)
    left: dp[i][j-1] (if not an obstacle)

    Finally, return the value in the bottom-right cell of the dp array. Which is the number of possible unique paths that the robot can take to reach the bottom-right corner.

'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        # Base case: If start cell itself is blocker, then 0 paths.
        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1

        # Fill first column
        for i in range(1, m):
            # current cell is not an obstacle and the previous cell in the row has a path
            if obstacleGrid[i][0] == 0 and dp[i - 1][0] == 1:
                dp[i][0] = 1

        # Fill first row
        for j in range(1, n):
            # current cell is not an obstacle and the previous cell in the row has a path
            if obstacleGrid[0][j] == 0 and dp[0][j - 1] == 1:
                dp[0][j] = 1

        # Fill rest of dp grid
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    # If current cell is not an obstacle, sum paths from top and left cells
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0  # Obstacle

        return dp[-1][-1]

'''
Follow-Up / Variations

    Unique Paths II: Some cells are blocked. You must avoid them.
        Use DP, but set dp[i][j] = 0 if cell is blocked.

    Minimum Path Sum: Each cell has a cost. Find the path with minimum total sum.
        Same DP idea, but use min() instead of +.

    Robot in a Grid with Obstacles: Like II, but ask for the actual path not just count.
        Backtrack with DP.

    Count all paths with K turns.
        Advanced DP, state includes (i, j, direction, turns).
'''
