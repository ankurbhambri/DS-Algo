# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

from collections import defaultdict


# TC: O(n^2)
# SC: O(n^2)
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:

        n = len(nums)

        dp = [defaultdict(int) for _ in range(n)]

        ans = 0

        for i in range(n):

            for j in range(i):

                d = nums[i] - nums[j]

                cnt = dp[j][d]

                ans += cnt

                dp[i][d] += cnt + 1

        return ans


print(Solution().numberOfArithmeticSlices([2, 4, 6, 8, 10]))  # Output: 7
print(Solution().numberOfArithmeticSlices([7, 7, 7, 7, 7]))  # Output: 16