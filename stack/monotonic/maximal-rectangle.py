from collections import deque

def maximalRectangle(matrix):

    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])         

    # 84. Largest Rectangle in Histogram
    def largestRectangleArea(heights):
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        q = deque()

        # Finding the nearest smaller to the left & right in a single pass
        for i in range(n):
            while q and heights[q[-1]] > heights[i]:  
                t = q.pop()
                right[t] = i  # Nearest smaller to the right for index t
            if q:
                left[i] = q[-1]  # Nearest smaller to the left for index i
            q.append(i)

        # Compute the maximum area
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            max_area = max(max_area, heights[i] * width)

        return max_area

    heights = [0] * cols  # Histogram representation
    max_area = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                heights[j] += 1  # Increase height
            else:
                heights[j] = 0  # Reset height

        # Apply largest rectangle in histogram on current row
        max_area = max(max_area, largestRectangleArea(heights))

    return max_area

print(maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))  # Output: 6
