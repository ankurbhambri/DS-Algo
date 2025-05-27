# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

'''
    Given an array of integers, and an integer N, find the length of the longest “N-stable” continuous subarray.
    An array is defined to be “N-stable” when the pair-wise difference between any two elements in the array is smaller or equal to N.
    A subarray of a 0-indexed integer array is a contiguous non-empty sequence of elements within an array.

    For instance, for array [ 4, 2, 3, 6, 2, 2, 3, 2, 7 ], and N = 1
    The return value should be 4, since the longest 1-stable subarray is [ 2, 2, 3, 2 ].
'''

from collections import deque

def func(arr, N):

    if not arr:
        return 0

    l = 0

    min_deque, max_deque = deque(), deque()

    res = 0

    for r in range(len(arr)):

        while min_deque and arr[min_deque[-1]] > arr[r]:
            min_deque.pop()
        min_deque.append(r)

        while max_deque and arr[max_deque[-1]] < arr[r]:
            max_deque.pop()
        max_deque.append(r)

        # processing
        while arr[max_deque[0]] - arr[min_deque[0]] > N:

            l += 1

            while min_deque and min_deque[0] < l:
                min_deque.popleft()

            while max_deque and max_deque[0] < l:
                max_deque.popleft()

        res = max(res, r - l + 1)

    return res

print(func([4, 2, 3, 6, 2, 2, 3, 2, 7], 1)) # 4
print(func([1, 2, 3, 4, 5], 2))  # Output: 3
print(func([1, 3, 6, 7, 8, 9], 3))  # Output: 4
print(func([10, 1, 2, 3, 4, 5], 5))  # Output: 6
