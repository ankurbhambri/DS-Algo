# https://leetcode.com/problems/largest-rectangle-in-histogram/description/


def largestRectangleArea(heights):

    n = len(heights)
    left = [-1] * n  # Nearest smaller to the left
    right = [n] * n  # Nearest smaller to the right
    stack = []

    # Find the nearest smaller to the left
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    stack = []

    # Find the nearest smaller to the right
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)

    # Compute the maximum area
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

heights = [2, 1, 2]
print(largestRectangleArea(heights))  # Output: 3

heights = [1, 2, 3, 4, 5]
print(largestRectangleArea(heights))  # Output: 9
