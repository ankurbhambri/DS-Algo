# https://leetcode.com/problems/count-square-submatrices-with-all-ones


'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.

'''

# DP, bottoms-up
class Solution:
    def countSquares(self, matrix):

        res = 0
        r, c = len(matrix), len(matrix[0])
        dp = [[0] * (c + 1) for _ in range(r + 1)]

        for i in range(r):
            for j in range(c):

                if matrix[i][j]:
                    # curr = 1 + min(left, dig, top)
                    dp[i + 1][j + 1] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i][j])

                    res += dp[i + 1][j + 1]
        return res

# Space optimised
class Solution:
    def countSquares(self, matrix):

        res = 0
        r, c = len(matrix), len(matrix[0]) 

        for i in range(r):
            for j in range(c):

                if matrix[i][j]:

                    dig = matrix[i - 1][j - 1] if i > 0 and j > 0 else 0
                    top = matrix[i - 1][j] if i > 0 else 0
                    left = matrix[i][j - 1] if j > 0 else 0

                    matrix[i][j] = 1 + min(dig, top, left)

                    res += matrix[i][j]
        return res