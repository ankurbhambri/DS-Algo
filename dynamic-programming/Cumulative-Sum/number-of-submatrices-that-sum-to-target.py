# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/

# This problem is a 560. Subarray Sum Equals K ka 2D version...., https://leetcode.com/problems/subarray-sum-equals-k/

from collections import Counter


# TC: O(n^3) -> 2 for loops for column boundaries and 1 for loop for row traversal
class Solution:
    def numSubmatrixSumTarget(self, matrix, target):

        m, n = len(matrix), len(matrix[0])

        # 1. In-place row-wise prefix sum (Perfect hai), jaise row1 = [1, 2, 3] ban jayega [1, 3, 6]
        for row in matrix:
            for i in range(n - 1):
                row[i + 1] += row[i]

        count = 0
        # 2. Column boundaries fix karna
        for col_start in range(n): # col_start = 0, 1, 2
            for col_end in range(col_start, n): # col_end = 0, 1, 2 (col_start se start hoke n-1 tak jayega)

                counter = Counter()
                counter[0] = 1
                curr_sum = 0

                # 3. Row-by-row travel karna
                for r in range(m): # r = 0, 1, 2

                    curr_sum += matrix[r][col_end] - (matrix[r][col_start - 1] if col_start > 0 else 0) # har row ke liye uski col_end aur col_start ke beech ka sum nikalna

                    count += counter[curr_sum - target]
                    counter[curr_sum] += 1

        return count


print(Solution().numSubmatrixSumTarget([[1,-1],[-1,1]], 0))
print(Solution().numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0))