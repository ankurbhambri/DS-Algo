# https://leetcode.com/problems/divisor-game/description/

# recursive solution with memoization
class Solution:
    def divisorGame(self, n: int) -> bool:

        memo = {}

        def helper(i):

            if i in memo:
                return memo[i]

            if i == 1:
                return False

            for j in range(1, i):
                if i % j == 0 and helper(i - j) == False:
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return helper(n)


# iterative solution
class Solution:
    def divisorGame(self, n: int) -> bool:

        if n == 1:
            return False

        dp = [False for i in range(n + 1)]

        for i in range(2, n + 1, 2):
            dp[i] = True

        return dp[n]


# Math solution: Alice wins if n is even, Bob wins if n is odd.
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0