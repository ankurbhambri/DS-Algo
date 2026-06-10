# Template for interval dynamic programming problems

class Solution:
    def solve(self, arr: list[int], cost) -> int:

        n = len(arr)

        dp = [[0] * n for _ in range(n)]

        # length = current interval size
        # 2 here, because we need at least 2 elements to make a valid interval (depends on problem)
        for length in range(2, n + 1):

            # start of interval
            for i in range(n - length + 1):

                # end of interval
                j = i + length - 1

                # initialize according to problem
                dp[i][j] = float("inf")      # min problems
                # dp[i][j] = 0               # max problems

                # try every split point
                for k in range(i, j):

                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k] + # left interval cost
                        dp[k + 1][j] + # right interval cost
                        cost(i, k, j) # cost of current split (depends on problem)
                    )

        return dp[0][n - 1]