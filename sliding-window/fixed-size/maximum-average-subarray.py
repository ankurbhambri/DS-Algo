# https://leetcode.com/problems/maximum-average-subarray-i/


# Question: Given an integer array nums and an integer k, return the maximum average value of any subarray of length k.
# Answers are being returned as an integer, so the answer will be truncated to an integer.
# If there are multiple answers, return the largest one.


# Note: The sliding window technique is used to maintain the sum of the current window of size k.
# The sum is updated by adding the next element and subtracting the first element of the previous window.
# The maximum sum is tracked, and the average is calculated at the end by dividing the maximum sum by k.
# The result is returned as a float, but it will be truncated to an integer when printed
# as per the problem statement.
# This approach ensures that we only traverse the array once, making it efficient for large inputs.


# Time Complexity: O(n)
# Space Complexity: O(1) for the variables
class Solution:
    def findMaxAverage(self, nums, k: int):

        sm = sum(nums[0:k])

        res = sm

        for r in range(k, len(nums)):

            sm += nums[r] - nums[r - k]

            res = max(res, sm)

        return res / k


print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4)) # 12.75
print(Solution().findMaxAverage([5], 1)) # 5.0
print(Solution().findMaxAverage([1, 2, 3, 4, 5], 2)) # 4.5
print(Solution().findMaxAverage([1, 2, 3, 4, 5], 3)) # 5.0


# https://leetcode.com/problems/maximum-average-subarray-iI/
