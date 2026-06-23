# https://leetcode.com/problems/maximal-rectangle/


# TC: O(m * n) where m is the number of rows and n is the number of columns in the matrix
# SC: O(n) for the heights array and stack
class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])

        def largestRectangleArea(heights):

            stack = []  # Stack to store indices of bars
            max_area = 0
            n = len(heights)

            for i in range(n + 1):

                # Dummy height 0 at the end to process remaining bars
                curr_height = 0 if i == n else heights[i]

                # Jab tak stack khali nahi aur current height top se chhoti hai
                while stack and heights[stack[-1]] > curr_height:

                    # Pop the top bar
                    idx = stack.pop()

                    height = heights[idx]

                    # Calculate width
                    width = i - stack[-1] - 1 if stack else i

                    # Calculate area and update max_area
                    max_area = max(max_area, height * width)

                # Push current index to stack
                stack.append(i)

            return max_area


        max_area = 0

        heights = [0] * cols  # Histogram representation

        for i in range(rows):

            for j in range(cols):

                if matrix[i][j] == '1':
                    heights[j] += 1  # Increase height

                else:
                    heights[j] = 0  # Reset height

            # Apply largest rectangle in histogram on current row
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area


print(Solution().maximalRectangle([["0"]]))  # Output: 0
print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))  # Output: 6