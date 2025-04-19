# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

def solution(nums, target):

    l, r = 0, len(nums) - 1

    while l <= r:

        m = l + (r - r) // 2

        if nums[m] == target:
            return m

        if nums[l] <= nums[m]: # left half is sorted
            if nums[l] <= target <= nums[m]:
                r = m - 1
            else:
                l = m + 1

        else: # right half is sorted
            if nums[m] <= target <= nums[r]:
                l = m + 1
            else:
                r = m - 1

    return -1
  
nums = [4, 5, 6, 7, 0, 1, 2]
target = 7
print(solution(nums, target))
