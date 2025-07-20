# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums, k: int):

        sm = sum(nums[0:k])

        res = sm

        for r in range(k, len(nums)):

            sm += nums[r] - nums[r - k]

            res = max(res, sm)

        return res / k


print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4)) # 12.75
print(Solution().findMaxAverage([5], 1)) # 5.0
print(Solution().findMaxAverage([1, 2, 3, 4, 5], 2)) # 4.5
print(Solution().findMaxAverage([1, 2, 3, 4, 5], 3)) # 5.0
