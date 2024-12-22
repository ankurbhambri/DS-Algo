# https://leetcode.com/problems/sliding-window-maximum/description/

from collections import deque


def maxSlidingWindow(nums, k):

    l = r = 0
    q = deque()
    res = []

    while r < len(nums):

        while q and nums[q[-1]] < nums[r]:
            q.pop()

        # appending pointer
        q.append(r)

        # To maintain the boundary of the sliding window, there might be cases where an index from the
        # lower boundary (l) still remains in the deque because its value is greater than other elements in the window.
        # However, since this index is no longer part of the current window,
        # we need to remove it from the deque to ensure the indices in the deque are within the window's range.

        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            res.append(nums[q[0]])
            l += 1
        r += 1

    return res


print(maxSlidingWindow([1], 1))  # Output: [1]
print(maxSlidingWindow([4, -2], 2))  # Output: [4]
print(maxSlidingWindow([9, 11], 2))  # Output: [11]
print(maxSlidingWindow([1, -1], 1))  # Output: [1,-1]
print(maxSlidingWindow([7, 2, 4], 2))  # Output: [7,4]
print(maxSlidingWindow([1, 3, 1, 2, 0, 5], 6))  # Output: [5]
print(maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))  # Output: [3,3,2,5]
print(maxSlidingWindow([1, 3, 1, 2, 0, 5], 1))  # Output: [1,3,1,2,0,5]
print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Output: [3,3,5,5,6,7]
