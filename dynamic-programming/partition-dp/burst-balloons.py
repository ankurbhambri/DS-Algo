# https://leetcode.com/problems/burst-balloons


# Recursive + memoization approach, O(n^3) Time Complexity and O(n^2) Space Complexity
class Solution:
    def maxCoins(self, nums):

        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):

            if l > r:
                return 0

            if (l, r) in dp:
                return dp[ (l, r)]

            dp[ (l, r)] = 0
            for i in range(1, r + 1):

                coins = nums [l - 1] * nums[i] * nums [r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)

                dp[(l, r)] = max(dp[(l, r)], coins)

            return dp[(l, r)]

        return dfs(1, len(nums) - 2)


# Bottom-up, O(n^3) Time Complexity and O(n^2) Space Complexity
class Solution:
    def maxCoins(self, nums):

        nums = [1] + nums + [1]
        n = len(nums)
        
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


print(Solution().maxCoins([3, 1, 5, 8]))  # Output: 167