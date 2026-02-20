# https://leetcode.com/problems/buildings-with-an-ocean-view/

'''
You are given an array of integers heights of size n representing a row of buildings, where heights[i] is the height of the ith building.

There is an ocean located to the far right of the buildings. A building has an ocean view if every building to its right is strictly shorter than it.

Return a list of indices (0-indexed) of the buildings that have an ocean view, sorted in increasing order.

Example 1:

Input: heights = [4,2,3,2,1]

Output: [0,2,3,4]
Example 2:

Input: heights = [1,3,2,4,2,5,1]

Output: [5,6]
Example 3:

Input: heights = [9,8,7,7,6,5,4,3]

Output: [0,1,3,4,5,6,7]
Constraints:

1 <= heights.length <= 100,000.
1 <= heights[i] <= 1,000,000,000

'''

# TC: O(n) where n is the length of heights
# SC: O(n) because we are using a stack to store indices of buildings with ocean view
class Solution:
    def findBuildings(self, heights):

        st = []
        for i in range(len(heights)):
            while st and heights[st[-1]] <= heights[i]:
                st.pop()
            st.append(i)
        return st

print(Solution().findBuildings([4,2,3,2,1])) # [0,2,3,4]
print(Solution().findBuildings([1,3,2,4,2,5,1])) # [5,6]
print(Solution().findBuildings([9,8,7,7,6,5,4,3])) # [0,1,3,4,5,6,7]

# The problem is conceptually simpler (and often cleaner) if we scan from right to left, since the ocean is on the right

class Solution:
    def findBuildings(self, heights):
        max_right = 0
        res = []
        
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_right:
                res.append(i)
                max_right = heights[i]
        
        return res[::-1]


# Variant: What happens if the buildings are on an island, and we need to also consider a left side view of the ocean?

class Solution:
    def findBuildingsIsland(self, heights):

        n = len(heights)

        right_view = [False] * n
        left_view = [False] * n

        # Right ocean (scan from right)
        max_right = 0
        for i in range(n - 1, -1, -1):
            if heights[i] > max_right:
                right_view[i] = True
                max_right = heights[i]

        # Left ocean (scan from left)
        max_left = 0
        for i in range(n):
            if heights[i] > max_left:
                left_view[i] = True
                max_left = heights[i]

        # Union: can see either ocean
        return [i for i in range(n) if left_view[i] or right_view[i]]

print(Solution().findBuildingsIsland([1,2,6,4,5])) # [0,1,2,4]