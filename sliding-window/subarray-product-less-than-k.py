# https://leetcode.com/problems/subarray-product-less-than-k/


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):

        if k <= 1:
            return 0

        prod = 1

        ans = left = 0

        for right, val in enumerate(nums):

            prod *= val

            while prod >= k:
                prod /= nums[left]
                left += 1

            ans += right - left + 1

        return ans


print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))  # Output: 8
print(Solution().numSubarrayProductLessThanK([1, 2, 3, 4], 10))  # Output: 7
print(Solution().numSubarrayProductLessThanK([1, 2, 3], 0))  # Output: 0
print(Solution().numSubarrayProductLessThanK([1, 2, 3], 1))  # Output: 0
