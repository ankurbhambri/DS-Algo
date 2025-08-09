# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/

# Question: Given an array of integers nums and an integer k, return the maximum length of a subarray that sums to k. If there is no such subarray, return 0.

def maxSubArrayLen(nums, k):

    max_len = 0
    seen = {0: -1}  # prefix_sum 0 at index -1 for edge case
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum - k in seen:
            max_len = max(max_len, i - seen[prefix_sum - k])

        # Only store first occurrence of a prefix_sum
        if prefix_sum not in seen:
            seen[prefix_sum] = i

    return max_len


print(maxSubArrayLen([1, -1, 5, -2, 3], 3))  # Output: 4
print(maxSubArrayLen([-2, -1, 2, 1], 1))  # Output: 2
print(maxSubArrayLen([1, 2, 3], 3))  # Output: 2
print(maxSubArrayLen([1, 2, 3], 6))  # Output: 3
