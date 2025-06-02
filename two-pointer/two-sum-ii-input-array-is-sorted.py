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

print(Solution().twoSum([2, 7, 11, 15], 9))  # [1, 2]
print(Solution().twoSum([2, 3, 4], 6))  # [1, 3]
print(Solution().twoSum([-1, 0], -1))  # [1, 2]
print(Solution().twoSum([5, 25, 75], 100))  # [2, 3]
print(Solution().twoSum([1, 2, 3, 4, 4, 5], 8))  # [4, 5]