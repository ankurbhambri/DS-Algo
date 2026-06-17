# https://leetcode.com/problems/missing-number/solution/


# Gauss' Formula
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        sm = sum(nums)
        t = (n * (n + 1)) // 2  # Gauss' Formula
        return t - sm

print(Solution().missingNumber([3, 0, 1]))  # Output: 2
print(Solution().missingNumber([0, 1]))  # Output: 2