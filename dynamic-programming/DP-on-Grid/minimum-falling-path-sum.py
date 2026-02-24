# https://leetcode.com/problems/minimum-falling-path-sum/description/

from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        R, C = len(matrix), len(matrix[0])

        for i in range(1, R):

            for j in range(C):

                up = matrix[i-1][j]
                left = matrix[i-1][j - 1] if j - 1 >= 0 else float("inf")
                right = matrix[i-1][j + 1] if j + 1 < C else float("inf")

                matrix[i][j] += min(up, left, right)
            

        return min(matrix[-1])


# https://leetcode.com/problems/minimum-falling-path-sum-ii/description/


# TC: O(R * C^2) where R is the number of rows and C is the number of columns in the input matrix.
# SC: O(1) if we modify the input matrix in place, otherwise O(R * C) if we use a separate DP matrix.

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:

        r, c = len(A), len(A[0])

        for i in range(1, r):

            for j in range(c):

                tmp = A[i - 1][:j] + A[i - 1][j + 1:]

                A[i][j] += min(tmp)

        return min(A[r - 1]) # min from last row


# TC: O(R * C) where R is the number of rows and C is the number of columns in the input matrix.
# SC: O(1) if we modify the input matrix in place, otherwise O(R) if we use a separate DP matrix.

class Solution:
    def minFallingPathSum(self, A):
        n = len(A)
        
        for i in range(1, n):
            # find min1 and min2 from previous row
            min1 = min2 = float('inf')
            idx1 = -1
            
            for j in range(n):
                if A[i-1][j] < min1:
                    min2 = min1
                    min1 = A[i-1][j]
                    idx1 = j
                elif A[i-1][j] < min2:
                    min2 = A[i-1][j]
            
            # update current row
            for j in range(n):
                if j == idx1:
                    A[i][j] += min2
                else:
                    A[i][j] += min1
        
        return min(A[-1])