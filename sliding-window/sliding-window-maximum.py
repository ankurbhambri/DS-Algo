# https://leetcode.com/problems/sliding-window-maximum/description/

from collections import deque

'''
    Idea, we can use a deque to keep track of the indices of the maximum elements in the current window.
    The deque will store indices in such a way that the values they point to are in decreasing order.
    When we slide the window, we remove indices that are out of the current window and also remove elements
    from the back of the deque that are smaller than the current element, ensuring that the front of the deque
    always contains the index of the maximum element for the current window.

    In the last will add the front of the deque to the result list, which will always be the maximum for that window.
'''

def maxSlidingWindow(nums, k):

    n = len(nums)
    result = []
    dq = deque()

    for r in range(n):

        # Remove indices outside the window
        if dq and dq[0] < r - k + 1:
            dq.popleft()

        # Remove elements from back of deque if they are less than current nums[r].
        while dq and nums[dq[-1]] < nums[r]:
            dq.pop()

        # Add the current element's index
        dq.append(r)

        # Start adding max elements to the result after we've processed first k elements
        if r >= k - 1:
            result.append(nums[dq[0]])

    return result


print(maxSlidingWindow([1], 1))  # Output: [1]
print(maxSlidingWindow([1, 3, 1, 2, 0, 5], 6))  # Output: [5]
print(maxSlidingWindow([1, 3, 1, 2, 0, 5], 1))  # Output: [1,3,1,2,0,5]
print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Output: [3,3,5,5,6,7]
