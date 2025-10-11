# https://leetcode.com/problems/minimum-size-subarray-sum/

# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a subarray whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target, nums):

        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):

            total += nums[r]

            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res


print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2
print(Solution().minSubArrayLen(4, [1, 4, 4]))  # 1
print(Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # 0
print(Solution().minSubArrayLen(11, [1, 2, 3, 4, 5]))  # 3
print(Solution().minSubArrayLen(15, [1, 2, 3, 4, 5]))  # 5
print(Solution().minSubArrayLen(100, [1, 2, 3, 4, 5]))  # 0
