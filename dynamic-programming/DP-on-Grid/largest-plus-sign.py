# https://leetcode.com/problems/largest-plus-sign/

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines):

        '''
        Problem states, We need to start with a grid full of 1s", meaning every cell initially can be part of a plus sign.
        Then, we will mark the mines (obstacles) as 0 to indicate those cells cannot be part of any plus sign
        '''
        grid = [[1] * n for _ in range(n)]
        
        # Step 1: Mark mines as 0
        for r, c in mines:
            grid[r][c] = 0

        # Step 2: Prepare 4 DP grids
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]

        # Step 3: Fill left and up
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    # + 1 means we can extend the plus sign
                    left[i][j] = left[i][j - 1] + 1 if j > 0 else 1
                    up[i][j] = up[i - 1][j] + 1 if i > 0 else 1

        # Step 4: Fill right and down
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                print(i, j, n)
                if grid[i][j] == 1:
                    # + 1 means we can extend the plus sign
                    right[i][j] = right[i][j + 1] + 1 if j < n - 1 else 1
                    down[i][j] = down[i + 1][j] + 1 if i < n - 1 else 1

        # Step 5: Find max order of plus sign
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    order = min(left[i][j], right[i][j], up[i][j], down[i][j])
                    res = max(res, order)

        return res


print(Solution().orderOfLargestPlusSign(5, [[4, 2]]))  # Output: 2
print(Solution().orderOfLargestPlusSign(1, []))  # Output: 1
print(Solution().orderOfLargestPlusSign(5, [[0, 0], [1, 1], [2, 2], [3, 3]]))  # Output: 1
print(Solution().orderOfLargestPlusSign(3, [[0, 0], [0, 1], [1, 0]]))  # Output: 1
print(Solution().orderOfLargestPlusSign(3, [[1, 1]]))  # Output: 1
