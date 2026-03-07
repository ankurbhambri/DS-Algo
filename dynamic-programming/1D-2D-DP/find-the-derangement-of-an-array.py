# D(n) = (n − 1) * (D(n − 1) + D(n − 2))


class Solution:
    def findDerangement(self, n: int) -> int:

        MOD = 10 ** 9 + 7

        if n == 1:
            return 0

        if n == 2:
            return 1

        dp = [0] * (n + 1)

        dp[1] = 0
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % MOD

        return dp[n]


print(Solution().findDerangement(1))  # 0
print(Solution().findDerangement(2))  # 1
print(Solution().findDerangement(3))  # 2
print(Solution().findDerangement(4))  # 9


# Space optimized version

class Solution:
    def findDerangement(self, n: int) -> int:

        MOD = 10 ** 9 + 7

        if n == 1:
            return 0

        if n == 2:
            return 1

        prev2 = 0
        prev1 = 1

        for i in range(3, n + 1):
            curr = (i - 1) * (prev1 + prev2) % MOD
            prev2 = prev1
            prev1 = curr

        return prev1


print(Solution().findDerangement(1))  # 0
print(Solution().findDerangement(2))  # 1
print(Solution().findDerangement(3))  # 2
print(Solution().findDerangement(4))  # 9