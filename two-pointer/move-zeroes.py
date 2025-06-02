# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums):
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
        return nums

print(Solution().moveZeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
print(Solution().moveZeroes([0]))  # Output: [0]
print(Solution().moveZeroes([1, 2, 3]))  # Output: [1, 2, 3]
print(Solution().moveZeroes([0, 0, 1, 2, 3]))  # Output: [1, 2, 3, 0, 0]
