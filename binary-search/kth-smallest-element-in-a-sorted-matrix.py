# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

from heapq import heappush, heappop

# TC: O(M * N * logK)
# Space: O(K)
class Solution:  # 184 ms, faster than 69.45%
    def kthSmallest(self, matrix, k):

        m, n = len(matrix), len(matrix[0])  # For general, matrix doesn't need to be a square
        maxHeap = []

        for r in range(m):
            for c in range(n):
                heappush(maxHeap, -matrix[r][c])
                if len(maxHeap) > k:
                    heappop(maxHeap)
        return -maxHeap[0]

print(Solution().kthSmallest([[1, 2], [1, 3]], 3))  # Output: 2
print(Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))  # Output: 13


# Time: O((M+N) * logD)
# Space: O(1)
class Solution:
    def kthSmallest(self, matrix, k):

        rows, cols = len(matrix), len(matrix[0])  # For general, the matrix need not be a square

        def countLessOrEqual(x):

            # Instead of linear matching we are using binary search to count the number of elements less than or equal to x in each row.
            # upper_bound returns the index of the first element that is greater than x, so it gives us the count of elements <= x.
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
            for r in range(rows):
                # at every row, we are finding the upper bound for x, which means the number of elements in that row that are less than or equal to x.
                cnt += upper_bound(matrix[r], x)
            return cnt

        l, r = matrix[0][0], matrix[-1][-1]

        while l <= r:

            x = (l + r) // 2

            '''
                We binary search to find the smallest ans in range [minOfMatrix ..... maxOfMatrix] such that countLessOrEqual(ans) >= k,
                where countLessOrEqual(x) is the number of elements that are less than or equal to x.
            '''
            if countLessOrEqual(x) >= k:
                r = x - 1  # try to looking for a smaller value in the l side

            else:
                l = x + 1  # try to looking for a bigger value in the r side

        return l

print(Solution().kthSmallest([[1, 2], [1, 3]], 3))  # Output: 2
print(Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))  # Output: 13
