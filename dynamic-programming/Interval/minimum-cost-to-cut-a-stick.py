# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/


# Recursive + memoization approach, O(n^3) Time Complexity and O(n^2) Space Complexity

class Solution:
    def minCost(self, n: int, cuts):

        memo = {}
        cuts = [0] + sorted(cuts) + [n]

        def cost(left, right):

            if right - left == 1:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            ans = float("inf")

            for mid in range(left + 1, right):
                ans = min(
                    ans, cost(left, mid) + cost(mid, right) + cuts[right] - cuts[left]
                )

            memo[(left, right)] = ans

            return ans
        
        return cost(0, len(cuts) - 1)


print(Solution().minCost(7, [1, 3, 4, 5]))  # Output: 16
print(Solution().minCost(9, [5, 6, 1, 4, 2]))  # Output: 22


# Bottom-up, O(n^3) Time Complexity and O(n^2) Space Complexity
class Solution:
    def minCost(self, n: int, cuts: list[int]) -> int:

        cuts.sort()
        cuts = [0] + cuts + [n]

        m = len(cuts)

        dp = [[0] * m for _ in range(m)]

        for length in range(2, m):

            for i in range(m - length):

                j = i + length

                dp[i][j] = float('inf')

                for k in range(i + 1, j):

                    dp[i][j] = min(dp[i][j], cuts[j] - cuts[i] + dp[i][k] + dp[k][j])

        return dp[0][m - 1]

print(Solution().minCost(7, [1, 3, 4, 5]))  # Output: 16
print(Solution().minCost(9, [5, 6, 1, 4, 2]))  # Output: 22