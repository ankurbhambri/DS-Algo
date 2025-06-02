# https://leetcode.com/problems/single-number/

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. Solve in linear complexity


class Solution:
    def singleNumber(self, nums):
        a = 0
        for n in nums:
            a ^= n
        return a


print(Solution().singleNumber([4, 1, 2, 1, 2]))
print(Solution().singleNumber([2, 2, 1]))
print(Solution().singleNumber([1]))
print(Solution().singleNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
print(Solution().singleNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
