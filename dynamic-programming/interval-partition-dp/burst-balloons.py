# https://leetcode.com/problems/burst-balloons


# Here, we are trying to find the maximum coins we can collect by bursting balloons in an optimal order.
# The idea is to consider each balloon as the last balloon to burst in a given interval [l, r].


# Recursive + memoization approach, O(n^3) Time Complexity and O(n^2) Space Complexity
class Solution:
    def maxCoins(self, nums):

        memo = {}
        nums = [1] + nums + [1]

        def helper(l, r):

            if l > r:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            memo[(l, r)] = 0

            for k in range(1, r + 1):

                # Consider balloon k as the last balloon to burst in interval [l, r]
                coins = nums[l - 1] * nums[k] * nums[r + 1]

                # Recursively calculate the maximum coins for the left and right subintervals
                coins += helper(l, k - 1) + helper(k + 1, r)

                # The total coins for this choice is the coins obtained by bursting balloon k last
                memo[(l, r)] = max(memo[(l, r)], coins)

            return memo[(l, r)]

        return helper(1, len(nums) - 2)


print(Solution().maxCoins([1, 5]))  # Output: 10
print(Solution().maxCoins([3, 1, 5, 8]))  # Output: 167


# Bottom-up, O(n^3) Time Complexity and O(n^2) Space Complexity
class Solution:
    def maxCoins(self, nums):

        n = len(nums)
        nums = [1] + nums + [1]

        # Initialize DP table
        dp = [[0] * n for _ in range(n)]

        # Iterate over all possible intervals
        for length in range(2, n):  # length is the distance between i and j
            for i in range(n - length):  # start index
                j = i + length  # end index
                # Calculate maximum coins for range [i, j]
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])

        # Result is the maximum coins for the whole range
        return dp[0][n - 1]


print(Solution().maxCoins([1, 5]))  # Output: 10
print(Solution().maxCoins([3, 1, 5, 8]))  # Output: 167