# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

from heapq import heappush, heappop

# TC: O(M * N * logK)
# SC: O(K)
class Solution:
    def kthSmallest(self, matrix, k):

        maxHeap = []
        m, n = len(matrix), len(matrix[0])  # For general, matrix doesn't need to be a square

        for r in range(m):
            for c in range(n):
                heappush(maxHeap, -matrix[r][c])
                if len(maxHeap) > k:
                    heappop(maxHeap)
        return -maxHeap[0]

print(Solution().kthSmallest([[1, 2], [1, 3]], 3))  # Output: 2
print(Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))  # Output: 13