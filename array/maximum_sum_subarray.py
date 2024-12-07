# similar questions
# - https://leetcode.com/problems/maximum-subarray/description/
# - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""

    Given an array with at least one positive integer, find the contiguous sub-array 
    with the largest sum.

    For example, for the sequence of values -2, 1, -3, 4, -1, 2, 1, -5, 4; 
    For eg. contiguous sub-array with the largest sum is 4, -1, 2, 1, with sum 6.

"""

# Used kadane's algorithm


def max_subarray_sum(arr):

    max_sum = float("-inf")
    current_sum = 0
    start = end = temp_start = 0

    for i in range(len(arr)):

        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

        # If current_sum becomes negative, reset it and update the temp_start index
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return max_sum, arr[start : end + 1]


a, b = max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print("Sub-array with maximum sum:", b, " Maximum sum:", a)

a, b = max_subarray_sum([5, 4, -1, 7, 8])
print("Sub-array with maximum sum:", b, " Maximum sum:", a)
