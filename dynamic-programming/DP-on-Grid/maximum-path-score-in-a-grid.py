# https://leetcode.com/problems/maximum-path-score-in-a-grid


class Solution:
    def maxPathScore(self, grid, k):

        m, n = len(grid), len(grid[0])

        # dp[i][j][c] = max score
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = 0

        for i in range(m):

            for j in range(n):

                for c in range(k + 1):

                    if dp[i][j][c] == -1:
                        continue

                    for dx, dy in [(1,0), (0,1)]:

                        ni, nj = i + dx, j + dy

                        if ni < m and nj < n:

                            cost = 1 if grid[ni][nj] > 0 else 0

                            nc = c + cost

                            if nc <= k:
                                dp[ni][nj][nc] = max(
                                    dp[ni][nj][nc],
                                    dp[i][j][c] + grid[ni][nj]
                                )

        ans = max(dp[m - 1][n - 1])

        return ans if ans != -1 else -1


print(Solution().maxPathScore([[0, 1],[2, 0]], 1))
print(Solution().maxPathScore([[0, 1],[1, 2]], 1))
print(Solution().maxPathScore([[0, 1, 2], [1, 0, 2], [0, 1, 0]], 2))