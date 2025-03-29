# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

from collections import deque

def largestRectangleArea(heights):

    n = len(heights)
    left = [-1] * n
    right = [n] * n

    q = deque()

    # Finding the nearest smaller to the left & right in a single pass
    for i in range(n):
        while q and heights[q[-1]] > heights[i]:
            t = q.pop()
            right[t] = i # Nearest smaller to the right for index t
        if q:
            left[i] = q[-1] # Nearest smaller to the left for index i

        q.append(i)

    max_area = 0
    for i in range(n):
        width = right[i] - left[i] - 1
        max_area = max(max_area, heights[i] * width)

    return max_area

# Example Usage
heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))  # Output: 10

heights = [2, 4]
print(largestRectangleArea(heights))  # Output: 4

heights = [2, 0, 2, 1, 1]
print(largestRectangleArea(heights))  # Output: 3

heights = [1, 2, 3, 4, 5]
print(largestRectangleArea(heights))  # Output: 9
