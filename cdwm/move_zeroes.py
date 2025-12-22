# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums) -> None:
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1


print(Solution().moveZeroes([0,1,0,3,12]))  # [1,3,12,0,0]


# VARIANT: What if you had to move zeroes to the front, not the back?

class Solution:
    def moveZeroesToFront(self, nums) -> None:
        r = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != 0:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1

print(Solution().moveZeroesToFront([0,1,0,3,12]))  # [0,0,1,3,12]