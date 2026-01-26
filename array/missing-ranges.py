# https://leetcode.com/problems/missing-ranges/description/

'''

You are given an inclusive range [lower, upper] and a sorted unique integer array nums, 
where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. 
That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99

Output: [[2,2], [4,49], [51,74], [76,99]]

Explanation: The ranges are:
    [2,2]
    [4,49]
    [51,74]
    [76,99]

Example 2:

Input: nums = [-1], lower = -1, upper = -1

Output: []

Explanation: There are no missing ranges since there are no missing numbers.
 

Constraints:

    -109 <= lower <= upper <= 109
    0 <= nums.length <= 100
    lower <= nums[i] <= upper
    All the values of nums are unique.

'''

# TC: O(n)
# SC: O(N)

class Solution:
    def findMissingRanges(self, nums, lower: int, upper: int):

        n = len(nums)

        if n == 0:
            return [[lower, upper]]
        
        missing_ranges = []

        if lower < nums[0]:
            missing_ranges.append([lower, nums[0] - 1])
        
        for i in range(1, n):
            if nums[i] - nums[i - 1] > 1:
                missing_ranges.append([nums[i - 1] + 1, nums[i] - 1])

        if upper > nums[-1]:
            missing_ranges.append([nums[-1] + 1, upper])
        
        return missing_ranges


print(Solution().findMissingRanges([-1], -1, -1))
print(Solution().findMissingRanges([0,1,3,50,75], 0, 99))

# VARIANTS:

    # What if there are more than 2 consecutive missing numbers?
    # What if there are exactly 2 consecutive missing numbers?
    # What if there is exactly 1 missing number?


