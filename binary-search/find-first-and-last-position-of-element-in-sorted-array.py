# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        
        # Helper function to find the lower and upper bounds        
        def helper(logic):
            l, r = 0, len(nums)
            while l < r:
                m = (l + r) // 2
                if logic(nums[m], target):
                    l = m + 1
                else:
                    r = m
            return l

        lower_bound = helper(lambda a, b: a < b)
        upper_bound = helper(lambda a, b: a <= b)

        # Validate target is actually in the range
        if lower_bound == len(nums) or nums[lower_bound] != target:
            return [-1, -1]

        return [lower_bound, upper_bound - 1]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
print(Solution().searchRange([], 0))  # [-1, -1]
print(Solution().searchRange([1], 1))  # [0, 0]
print(Solution().searchRange([1, 2, 3, 4, 5], 3))  # [2, 2]
