# https://leetcode.com/problems/stone-game-v/


# Recusion + Memoization approach
# TC: O(n^3) - three nested loops
# SC: O(n^2) - dp table
class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:

        n = len(stoneValue)

        ps = [0] * (n)
        ps[0] = stoneValue[0]

        for i in range(1, n):
            ps[i] = stoneValue[i] + ps[i - 1]
        
        memo = {}

        def solve(l, r):

            if l == r:
                return 0
            
            if (l, r) in memo:
                return memo[(l, r)]

            score = 0

            for i in range(l, r):

                lsum = ps[i] - ps[l] + stoneValue[l]

                rsum = ps[r] - ps[i]

                if lsum < rsum:
                    score = max(score, lsum + solve(l, i))

                elif lsum > rsum:
                    score = max(score, rsum + solve(i + 1, r))

                else:
                    score = max(score, lsum + solve(l, i), rsum + solve(i + 1, r))

            memo[(l, r)] = score
            return score

        return solve(0, n - 1)


# TC: O(n^3) - three nested loops
# SC: O(n^2) - dp table
class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:

        n = len(stoneValue)

        ps = [0] * n
        ps[0] = stoneValue[0]

        for i in range(1, n):
            ps[i] = ps[i - 1] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):

            for i in range(n - length + 1):

                j = i + length - 1

                for k in range(i, j):

                    lsum = ps[k] - (ps[i - 1] if i > 0 else 0)
                    rsum = ps[j] - ps[k]

                    if lsum < rsum:
                        dp[i][j] = max(dp[i][j], lsum + dp[i][k])

                    elif lsum > rsum:
                        dp[i][j] = max(dp[i][j], rsum + dp[k + 1][j])

                    else:
                        dp[i][j] = max(dp[i][j], lsum + dp[i][k], rsum + dp[k + 1][j])

        return dp[0][n - 1]