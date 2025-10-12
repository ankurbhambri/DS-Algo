# https://leetcode.com/problems/maximum-total-damage-with-spell-casting

from collections import Counter
from bisect import bisect_right


class Solution:
    def maximumTotalDamage(self, power):

        cnt = Counter(power)
        nums = sorted(cnt.keys())

        # number * occurrence
        damage = [x * cnt[x] for x in nums]

        dp = [0] * len(nums)

        for i in range(len(nums)):

            # Find last index j where nums[j] < nums[i] - 2
            j = bisect_right(nums, nums[i] - 3) - 1

            take = damage[i] + (dp[j] if j >= 0 else 0)
            skip = dp[i - 1] if i > 0 else 0

            dp[i] = max(take, skip)

        return dp[-1]


print(Solution().maximumTotalDamage([2,2,3,3,3,4]))  # Output: 9
print(Solution().maximumTotalDamage([3,4,2]))  # Output: 6
print(Solution().maximumTotalDamage([8,10,4,9,1,3,5,9,4,10]))  # Output: 37
print(Solution().maximumTotalDamage([1,1,1,2,4,5,5,5,6]))  # Output: 18
