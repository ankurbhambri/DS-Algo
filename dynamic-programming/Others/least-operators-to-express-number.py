# https://leetcode.com/problems/least-operators-to-express-number/


class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:

        memo = {}

        def cost(i):
            return i if i > 0 else 2

        def dp(i, target):

            if target == 0:
                return 0

            if (i, target) in memo:
                return memo[(i, target)]

            if target == 1:
                return cost(i)

            if i >= 39:
                return target + 1

            t = target // x
            r = target % x

            ans = min(
                r * cost(i) + dp(i + 1, t),
                (x - r) * cost(i) + dp(i + 1, t + 1)
            )

            memo[(i, target)] = ans

            return ans

        return dp(0, target) - 1


print(Solution().leastOpsExpressTarget(3, 19))
print(Solution().leastOpsExpressTarget(5, 501))