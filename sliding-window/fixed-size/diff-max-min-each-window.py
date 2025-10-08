# Given an array nums and an integer k, find the maximum difference between the maximum and minimum values in each sliding window of size k.

from collections import deque

def max_diff_in_window(nums, k):

    res = []
    max_q, min_q = deque(), deque()

    for i in range(len(nums)):

        while max_q and nums[max_q[-1]] < nums[i]:
            max_q.pop()

        while min_q and nums[min_q[-1]] > nums[i]:
            min_q.pop()

        max_q.append(i)
        min_q.append(i)

        if max_q[0] <= i - k:
            max_q.popleft()

        if min_q[0] <= i - k:
            min_q.popleft()

        if i >= k - 1:
            res.append(nums[max_q[0]] - nums[min_q[0]])

    return res


print(max_diff_in_window([1,3,-1,-3,5,3,6,7], 3))  # Output: [4, 6, 8, 8, 3, 4]
print(max_diff_in_window([1,2,3,4,5], 2))  # Output: [1, 1, 1, 1]
print(max_diff_in_window([5,4,3,2,1], 3))  # Output: [2, 2, 2]
print(max_diff_in_window([1, 2, 3, 4, 5], 1))  # Output: [0, 0, 0, 0, 0]
