# https://www.geeksforgeeks.org/dsa/longest-decreasing-subsequence/

class Solution:
    def longestDecreasingSubsequence(self, nums: list[int]) -> int:

        n = len(nums)

        dp = [1] * n

        for i in range(n):
            for j in range(i):
                # longest increasing subsequence mein bas yha hum sign change kar dente hain - if nums[i] > nums[j], else everything is same
                if nums[i] < nums[j]:

                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

print(Solution().longestDecreasingSubsequence([15, 27, 14, 38, 63, 55, 46, 65, 85])) # 3