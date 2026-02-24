# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

class Solution:
    def longestIncreasingPath(self, matrix):

        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])

        memo = [[-1] * cols for _ in range(rows)]

        def dfs(i, j, prev_val):

            # out of bounds ya current value chhota/equal hai prev value se
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
            memo[i][j] = 1 + max(up, down, left, right)

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


# Variation: Where we can traverse only if the number is consecutively increasing like 1->2->3->4
class Solution:
    def longestConsecutivePath(self, matrix):

        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = [[-1] * cols for _ in range(rows)]

        def dfs(r, c):

            # If already computed, return the cached value
            if memo[r][c] != -1:
                return memo[r][c]

            max_path = 1 # Every cell is a path of length 1

            # Directions: Up, Down, Left, Right
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

                nr, nc = r + dr, c + dc

                # Check bounds AND the Consecutive Condition: next must be current + 1
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == matrix[r][c] + 1:
                    max_path = max(max_path, 1 + dfs(nr, nc))

            memo[r][c] = max_path
            return max_path

        longest = 0
        for i in range(rows):
            for j in range(cols):
                longest = max(longest, dfs(i, j))

        return longest


# Standard increasing: 1->2->3->4 (Length 4)
# Here: 1->2->3 (Only if they are +1)
print(Solution().longestConsecutivePath([[1, 2], [4, 3]])) # Output: 4 (1-2-3-4)
print(Solution().longestConsecutivePath([[1, 3], [2, 4]])) # Output: 2 (1-2 or 3-4, but not 1-3)
print(Solution().longestConsecutivePath([[1, 2, 9], [5, 3, 8], [4, 6, 7]])) # Path: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 (Total 9)