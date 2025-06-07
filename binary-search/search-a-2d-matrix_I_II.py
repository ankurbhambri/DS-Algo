# https://leetcode.com/problems/search-a-2d-matrix/

# Think in a way that a 1 D row and find our a mid then get i, and j with formula and search in matrix

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])
     
        l = 0
        r = (row * col) - 1 # if we have 12 elements in entire matric then this will give the boundary 11, 0 based indexing.

        while l <= r:

            m = (l + r) // 2

            # To get (i, j) simple formula

            i, j = m // col, m % col

            if matrix[i][j] == target:
                return True

            elif matrix[i][j] > target:
                r = m - 1

            else:
                l = m + 1

        return False

print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))  # True
print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))  # False


# https://leetcode.com/problems/search-a-2d-matrix-ii/description/

# Idea: Start from the bottom-left corner of the matrix and move right when the value is smaller than the target or move up when the value is greater than the target.

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])

        c = 0
        r = row - 1

        while r >= 0 and c < col:

            if matrix[r][c] == target:
                return True

            if matrix[r][c] < target:
                c += 1

            else:
                r -= 1

        return False

print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))  # True
print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))  # False
print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60))  # True
print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1))  # True
