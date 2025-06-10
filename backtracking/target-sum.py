# https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:

        memo = {}

        def helper(idx, sm):

            if (idx, sm) in memo:
                return memo[(idx, sm)]

            if idx == len(nums):

                return 1 if sm == target else 0

            memo[(idx, sm)] = (helper(idx + 1, sm + nums[idx]) + helper(idx + 1, sm - nums[idx]))

            return memo[(idx, sm)]

        return helper(0, 0)

print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))  # Output: 5
print(Solution().findTargetSumWays([1], 1))  # Output: 1
print(Solution().findTargetSumWays([1, 2, 3], 4))  # Output: 3
print(Solution().findTargetSumWays([1, 2, 3, 4], 5))  # Output: 4
