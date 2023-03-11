# https://leetcode.com/problems/unique-paths/submissions/

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
        dp = [[1 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


# space optimization
# TC = O(M * N)
# SC = O(N)

def uniquePaths(m, n):
	prev_row = [0] * n
	prev_row[0] = 1
	for i in range(m):
		tmp = [0] * n
		for j in range(n):
			if i == 0 and j == 0:
				tmp[j] = 1
			else:
				tmp[j] = prev_row[j] + tmp[j - 1]
		prev_row = tmp
	return prev_row[-1]
