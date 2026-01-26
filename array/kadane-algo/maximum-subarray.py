# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums):

        n = len(nums)
        current_sum = 0  # Current sum
        max_sum = float("-inf")  # Initialize max to negative infinity

        for i in range(n):

            current_sum += nums[i]  # Add the current element to the running sum

            # Update the global maximum if the current sum is greater
            max_sum = max(max_sum, current_sum)

            # If the running sum becomes negative, reset it to 0
            if current_sum < 0:
                current_sum = 0

        return max_sum


print(Solution().maxSubArray([5, 4, -1, 7, 8]))  # 23
print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6


# Varinat: Return the subarray and the maximum sum

"""
Given an array with at least one positive integer, find the contiguous sub-array 
with the largest sum.

For example, for the sequence of values -2, 1, -3, 4, -1, 2, 1, -5, 4; 
the contiguous sub-array with the largest sum is 4, -1, 2, 1, with sum 6.

How It Works in the Example:

Consider the input [-2, 1, -3, 4, -1, 2, 1, -5, 4]:

Iteration details with variables (start, end, temp_start):
Index (i)  nums[i]  current_sum  max_sum  temp_start  start  end
0          -2      -2           -2       0           0      0
1          1       1            1        1           1      1
2          -3      -2           1        2           1      1
3          4       4            4        3           3      3
4          -1      3            4        3           3      3
5          2       5            5        3           3      5
6          1       6            6        3           3      6
7          -5      1            6        3           3      6
8          4       5            6        3           3      6

Result: Maximum sum is 6, and the subarray is [4, -1, 2, 1].
"""


def max_subarray_sum(nums):

    max_sum = float("-inf")
    current_sum = 0
    start = end = temp_start = 0

    for i in range(len(nums)):

        current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

        # If current_sum becomes negative, reset it and update the temp_start index
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return max_sum, nums[start : end + 1]


print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # (6, [4, -1, 2, 1])
print(max_subarray_sum([5, 4, -1, 7, 8]))  # (23, [5, 4, -1, 7, 8])
