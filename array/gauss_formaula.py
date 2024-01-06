# https://leetcode.com/problems/missing-number/solution/


# Gauss' Formula
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        sm = sum(nums)
        t = (n * (n + 1)) // 2  # Gauss' Formula
        return t - sm
