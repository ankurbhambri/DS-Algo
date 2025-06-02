# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Find the smallest value” → use the cleaner comparison with nums[m] and nums[r]. While finding a specific value in a rotated array” → use binary search approach (check which half is sorted).

class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            # If mid element is greater than right, min must be in right half
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m  # min is at mid or in left half

        return nums[l]  # or nums[r], since l == r


print(Solution().findMin([3, 4, 5, 1, 2]))  # Output: 1
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))  # Output: 0
print(Solution().findMin([11, 13, 15, 17]))  # Output: 11
print(Solution().findMin([2, 1]))  # Output: 1
