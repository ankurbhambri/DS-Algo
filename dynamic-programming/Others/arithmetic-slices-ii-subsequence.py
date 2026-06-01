# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:

        res = 0
        n = len(nums)

        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):

                diff = nums[i] - nums[j]
                dp[i][diff] += 1 + dp[j][diff]
                res += dp[j][diff]

        return res


print(Solution().numberOfArithmeticSlices([2, 4, 6, 8, 10]))  # Output: 7
print(Solution().numberOfArithmeticSlices([7, 7, 7, 7, 7]))  # Output: 16