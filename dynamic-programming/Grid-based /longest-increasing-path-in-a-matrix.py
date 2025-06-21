# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

class Solution:
    def longestIncreasingPath(self, matrix):

        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        # Memoization cache to store the longest path from each cell
        memo = [[-1] * cols for _ in range(rows)]
        
        def dfs(i, j, prev_val):
            # Base cases: out of bounds ya value chhota/equal hai
            if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] <= prev_val:
                return 0
            
            # Agar memo mein already calculated hai, toh return kar do
            if memo[i][j] != -1:
                return memo[i][j]
            
            # Current cell se 4 directions mein explore karo
            current = matrix[i][j]
            up = dfs(i-1, j, current)
            down = dfs(i+1, j, current)
            left = dfs(i, j-1, current)
            right = dfs(i, j+1, current)
            
            # Sabse lamba path choose karo aur +1 for current cell
            memo[i][j] = max(up, down, left, right) + 1
            return memo[i][j]
        
        # Har cell se start karke max path length find karo
        max_length = 0
        for i in range(rows):
            for j in range(cols):
                max_length = max(max_length, dfs(i, j, float('-inf')))
        
        return max_length


print(Solution().longestIncreasingPath([[1]]))  # Output: 1
print(Solution().longestIncreasingPath([[1,2],[3,4]]))  # Output: 3
print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))  # Output: 4
print(Solution().longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))  # Output: 4
