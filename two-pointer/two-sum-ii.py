# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# Similar to 1. Two Sum problem but here the input array is sorted. But here we have to use constant space.

class Solution:
    def twoSum(self, nums, target):

        n = len(nums)
        l, r = 0, n - 1

        while l <= r:

            if nums[l] + nums[r] == target:
                return [l + 1, r + 1]

            elif nums[l] + nums[r] < target:
                l += 1

            else:
                r -= 1

        return -1


print(Solution().twoSum([-1, 0], -1))  # [1, 2]
print(Solution().twoSum([2, 3, 4], 6))  # [1, 3]
print(Solution().twoSum([1, 2, 3, 4, 5], 10))  # -1
print(Solution().twoSum([2, 7, 11, 15], 9))  # [1, 2]