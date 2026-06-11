# https://leetcode.com/problems/remove-boxes/description


'''
Time: O(N^4), where N <= 100 is length of boxes array.
Explain: There is total N^3 dp states, they are dp[0][0][0], dp[0][0][1],..., dp[n][n][n], each state needs a loop O(N) to compute the result. So total complexity is O(N^4).
Space: O(N^3)

'''

from functools import lru_cache

class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        
        @lru_cache(None)
        def calculate(i, j, k):
            if i > j:
                return 0
            
            # Optimization: Collapse consecutive identical boxes
            # If boxes[i] == boxes[i+1], we might as well group them into 'k' right now
            while i + 1 <= j and boxes[i] == boxes[i + 1]:
                i += 1
                k += 1
                
            # Choice 1: Remove boxes[i] and its k neighbors immediately
            res = (k + 1) * (k + 1) + calculate(i + 1, j, 0)
            
            # Choice 2: Look for a matching box 'm' later in the array
            for m in range(i + 1, j + 1):
                if boxes[m] == boxes[i]:
                    # Clear middle section, and carry over (k + 1) to index m
                    points = calculate(i + 1, m - 1, 0) + calculate(m, j, k + 1)
                    res = max(res, points)
                    
            return res
            
        return calculate(0, len(boxes) - 1, 0)


print(Solution().removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1])) # 23