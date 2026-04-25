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
    def minCost(self, n: int, cuts):

        c = len(cuts)
        cuts = [0] + sorted(cuts) + [n]

        dp = [[0] * c for _ in range(c)]

        for length in range(2, c):
            
            # here, c - length is the number of intervals of the given length
            for l in range(c - length):

                r = l + length

                dp[l][r] = float('inf')

                for m in range(l + 1, r):

                    cost = dp[l][m] + dp[m][r] + cuts[r] - cuts[l]

                    dp[l][r] = min(dp[l][r], cost)

        return dp[0][c - 1]


print(Solution().minCost(7, [1, 3, 4, 5]))  # Output: 16
print(Solution().minCost(9, [5, 6, 1, 4, 2]))  # Output: 22