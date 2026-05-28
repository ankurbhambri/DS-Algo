# https://leetcode.com/problems/maximal-square/description/


# TC: O(m * n)
# SC: O(m * n)

class Solution:
    def maximalSquare(self, matrix):

        if not matrix or not matrix[0]:
            return 0

        res = 0
        r, c = len(matrix), len(matrix[0])
        dp = [[0] * c for _ in range(r)]

        # Fill the DP table from bottom-right to top-left
        for i in range(r - 1, -1, -1):
            for j in range(c - 1, -1, -1):

                if matrix[i][j] == "1":

                    if i == r - 1 or j == c - 1:
                        dp[i][j] = 1  # Edge cells only form size 1 squares

                    else:
                        dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])

                    res = max(res, dp[i][j])

        return res * res  # Return the area of the largest square


print(Solution().maximalSquare(
    [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
))  # Output: 4
print(Solution().maximalSquare([["0","1"], ["1","0"]]))  # Output: 1