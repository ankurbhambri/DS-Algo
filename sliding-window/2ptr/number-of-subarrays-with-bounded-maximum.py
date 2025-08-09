# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

class Solution:
    def numSubarrayBoundedMax(self, nums, left: int, right: int) -> int:
        def countBounded(bound):
            curr = 0
            count = 0
            for num in nums:
                if num <= bound:
                    curr += 1
                else:
                    curr = 0
                count += curr
            return count
        
        return countBounded(right) - countBounded(left - 1)


print(Solution().numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))  # Output: 3
print(Solution().numSubarrayBoundedMax([1, 2, 3, 4], 2, 3))  # Output: 6
print(Solution().numSubarrayBoundedMax([1, 2, 3, 4], 1, 4))  # Output: 10
print(Solution().numSubarrayBoundedMax([1, 2, 3, 4], 3, 3))  # Output: 4
