# https://leetcode.com/problems/number-of-longest-increasing-subsequence


class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:

        if not nums:
            return 0

        n = len(nums)

        dp = [1] * n
        count = [1] * n

        for i in range(n):

            for j in range(i):

                if nums[i] > nums[j]:

                    if dp[j] + 1 > dp[i]:

                        dp[i] = dp[j] + 1
                        count[i] = count[j]

                    elif dp[j] + 1 == dp[i]:

                        count[i] += count[j]

        ans = 0
        max_len = max(dp)

        for i in range(n):

            if dp[i] == max_len:

                ans += count[i]

        return ans


print(Solution().findNumberOfLIS([1, 3, 5, 4, 7]))  # Output: 2
print(Solution().findNumberOfLIS([2, 2, 2, 2, 2]))  # Output: 5