# https://leetcode.com/problems/minimum-falling-path-sum/


# memoization
# TC O(M * N)
# SC (M * N) + Stack space
def minFallingPathSum(vec, n):
    m = len(vec[0])
    memo = [[-1 for _ in range(m)] for _ in range(n)]

    def helper(i, j):
        if j < 0 or j >= m:
            return float("inf")
        if i == 0:
            memo[i][j] = vec[i][j]
            return vec[i][j]
        if memo[i][j] != -1:
            return memo[i][j]
        up = vec[i][j] + helper(i - 1, j)
        left_up = vec[i][j] + helper(i - 1, j - 1)
        right_up = vec[i][j] + helper(i - 1, j + 1)
        memo[i][j] = min(up, left_up, right_up)
        return memo[i][j]

    res = float("inf")
    for i in range(n):
        res = min(res, helper(n - 1, i))
    return res


# tabulation
# TC O(M * N)
# SC (M * N)
class Solution:
    def minFallingPathSum(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = matrix[0]
        for i in range(1, m):
            for j in range(n):
                up = matrix[i][j] + dp[i - 1][j]
                left_up = matrix[i][j] + (
                    dp[i - 1][j - 1] if j - 1 >= 0 else float("inf")
                )
                right_up = matrix[i][j] + (
                    dp[i - 1][j + 1] if j + 1 < n else float("inf")
                )
                dp[i][j] = min(up, left_up, right_up)
        return min(dp[m - 1])


# space optimization
# TC O(M * N)
# SC (N)
class Solution:
    def minFallingPathSum(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0])
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        prev = matrix[0]
        for i in range(1, m):
            tmp = [0] * n
            for j in range(n):
                up = matrix[i][j] + prev[j]
                left_up = matrix[i][j] + (prev[j - 1] if j - 1 >= 0 else float("inf"))
                right_up = matrix[i][j] + (prev[j + 1] if j + 1 < n else float("inf"))
                tmp[j] = min(up, left_up, right_up)
            prev = tmp
        return min(prev)
