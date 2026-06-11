# https://leetcode.com/problems/arithmetic-slices/


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]):

        curr = 0
        ans = 0

        for i in range(2, len(nums)):

            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                curr += 1
                ans += curr
            else:
                curr = 0

        return ans