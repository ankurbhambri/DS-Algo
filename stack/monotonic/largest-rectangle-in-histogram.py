# https://leetcode.com/problems/largest-rectangle-in-histogram/description/


# TC: O(n) where n is the number of bars in the histogram
# SC: O(n) for the stack
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

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