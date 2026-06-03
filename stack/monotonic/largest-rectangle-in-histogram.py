# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

from collections import deque

# TC: O(n)
# SC: O(n)

# Using two arrays to store the nearest smaller to the left and right for each index
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        n = len(heights)
        left = [-1] * n
        right = [n] * n

        q = deque()

        # Finding the nearest smaller to the left & greater to the right for each index
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


# TC: O(n)
# SC: O(n)

# Using a stack to store indices of bars and calculating area when we encounter a smaller height
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        
        n = len(heights)
        stack = []  # Stack to store indices of bars
        max_area = 0
        
        for i in range(n + 1):

            # Dummy height 0 at the end to process remaining bars
            curr_height = 0 if i == n else heights[i]
            
            # Jab tak stack khali nahi aur current height top se chhoti hai
            while stack and heights[stack[-1]] > curr_height:
                # Pop the top bar
                idx = stack.pop()
                height = heights[idx]
                # Calculate width
                width = i - idx if stack else i
                # Calculate area and update max_area
                max_area = max(max_area, height * width)
            
            # Push current index to stack
            stack.append(i)
        
        return max_area