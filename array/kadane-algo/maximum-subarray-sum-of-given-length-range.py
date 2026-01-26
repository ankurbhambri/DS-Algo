# https://cs.stackexchange.com/questions/151165/maximum-subarray-sum-of-given-length-range

# https://cses.fi/problemset/task/1644

'''
Given an array of both negative and positive numbers, we want to find the maximum sum of the elements in contiguous subarray having a length between 𝑎
 and 𝑏
.

Example

Input:

8 1 2

-1 13 -2 5 13 -5 2 2

Output: 18

Here a = 1 , b = 2

Although Maximum sum is 29, Max sum of length between [1-2] is 18

'''

from collections import deque

# TC: O(n)
# SC: O(n)
def max_sum_subarray_in_range(nums, a, b):
    n = len(nums)
    
    # Compute prefix sum array
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]
    
    max_sum = float('-inf')
    dq = deque()  # Will store indices of prefix sum
    
    for i in range(1, n + 1):
        # Maintain a window of prefix indices in [i - b, i - a]
        if i - a >= 0:
            # Add prefix[i - a] as a candidate
            while dq and prefix[dq[-1]] >= prefix[i - a]:
                dq.pop()

            dq.append(i - a)
        
        # Remove elements out of window (less than i - b)
        while dq and dq[0] < i - b:
            dq.popleft()
        
        # Calculate max_sum using the min prefix in range
        if dq:
            max_sum = max(max_sum, prefix[i] - prefix[dq[0]])
    
    return max_sum

print(max_sum_subarray_in_range([-1, 13, -2, 5, 13, -5, 2, 2], 1, 2))  # Output: 18
print(max_sum_subarray_in_range([1, 2, 3, -2, 5], 1, 3))  # Output: 6
print(max_sum_subarray_in_range([-2, 1, -3, 4, -1, 2, 1, -5, 4], 1, 3))  # Output: 5
print(max_sum_subarray_in_range([5, -3, 5, 5, -3, 5], 1, 3))  # Output: 10
