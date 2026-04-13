'''
    Given an array of integers and a positive integer k, find the maximum sum of a subarray of size less than or equal to k. 
    A subarray is a contiguous part of the array. For example, if the array is [5, -3, 5, 5, -3, 5] and k is 3, 
    then the maximum subarray sum with at most k elements is 10, which is obtained by the subarray [5, 5]
'''

from collections import deque

# TC: O(n)
# SC: O(n)
def max_sum_subarray_at_most_k(arr, k):
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]

    max_sum = float('-inf')
    dq = deque()
    dq.append(0)

    for i in range(1, n + 1):
        # Remove indices from front if they are out of range (i - k)
        while dq and dq[0] < i - k:
            dq.popleft()
        max_sum = max(max_sum, prefix[i] - prefix[dq[0]])
        # Maintain monotonicity
        while dq and prefix[dq[-1]] >= prefix[i]:
            dq.pop()
        dq.append(i)

    return max_sum


print(max_sum_subarray_at_most_k([5, -3, 5, 5, -3, 5], 3))  # Output: 10
print(max_sum_subarray_at_most_k([-2, 1, -3, 4, -1, 2, 1, -5, 4], 3))  # Output: 5
print(max_sum_subarray_at_most_k([1, -2, 0, 3], 2))  # Output: 3
print(max_sum_subarray_at_most_k([-1, -1, -1, -1], 2))  # Output: -1
print(max_sum_subarray_at_most_k([5, 4, -1, 7, 8], 3))  # Output: 15
