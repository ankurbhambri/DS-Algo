class Solution:
    def minDays(self, n: int) -> int:

        memo = {}

        def helper(n):

            if n < 3:
                return n

            if n in memo:
                return memo[n]

            memo[n] = 1 + min(n % 2 + helper(n // 2), n % 3 + helper(n // 3))

            return memo[n]

        return helper(n)