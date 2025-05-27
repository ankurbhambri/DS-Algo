# https://leetcode.com/problems/sliding-window-maximum/description/

from collections import deque


def maxSlidingWindow(arr, k):

    n = len(arr)
    result = []
    dq = deque()

    for i in range(n):
        # Remove indices outside the window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove elements not smaller than the current element
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        # Add the current element's index
        dq.append(i)

        # Start adding max elements to the result after we've processed first k elements
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


print(maxSlidingWindow([1], 1))  # Output: [1]
print(maxSlidingWindow([4, -2], 2))  # Output: [4]
print(maxSlidingWindow([9, 11], 2))  # Output: [11]
print(maxSlidingWindow([1, -1], 1))  # Output: [1,-1]
print(maxSlidingWindow([7, 2, 4], 2))  # Output: [7,4]
print(maxSlidingWindow([1, 3, 1, 2, 0, 5], 6))  # Output: [5]
print(maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))  # Output: [3,3,2,5]
print(maxSlidingWindow([1, 3, 1, 2, 0, 5], 1))  # Output: [1,3,1,2,0,5]
print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Output: [3,3,5,5,6,7]
