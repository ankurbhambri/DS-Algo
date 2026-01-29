# https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/description/

'''

Given an m x n matrix grid containing an odd number of integers where each row is sorted in non-decreasing order, return the median of the matrix.

You must solve the problem in less than O(m * n) time complexity.

Example 1:

Input: grid = [[1,1,2],[2,3,3],[1,3,4]]
Output: 2
Explanation: The elements of the matrix in sorted order are 1,1,1,2,2,3,3,3,4. The median is 2.

Example 2:

Input: grid = [[1,1,3,3,4]]
Output: 3
Explanation: The elements of the matrix in sorted order are 1,1,3,3,4. The median is 3.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
m and n are both odd.
1 <= grid[i][j] <= 106

grid[i] is row-wise sorted in non-decreasing order.

'''

class Solution:
    def median(self, grid) -> int:

        def countLessOrEqual(x):

            def upper_bound(row, target):
                left, right = 0, len(row)
                while left < right:
                    mid = (left + right) // 2
                    if row[mid] <= target:
                        left = mid + 1
                    else:
                        right = mid
                return left

            cnt = 0
            for r in range(m):
                cnt += upper_bound(grid[r], x)
            return cnt

        l, r = 1, 10**6
        m, n = len(grid), len(grid[0])

        med = (m * n) // 2 + 1  # since m * n is odd

        while l <= r:

            x = (l + r) // 2

            if countLessOrEqual(x) >= med:
                r = x - 1
            else:
                l = x + 1

        return l

print(Solution().median([[1,1,3,3,4]]))  #  Output: 3
print(Solution().median([[1,1,2],[2,3,3],[1,3,4]]))  # Output: 2