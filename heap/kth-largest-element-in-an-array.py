# https://leetcode.com/problems/kth-largest-element-in-an-array/

from heapq import heappush, heappop


# TC: O(N log K)
# SC: O(K)
class Solution:
    def findKthLargest(self, nums, k: int) -> int:

        hm = []

        for i in nums:

            heappush(hm, i)

            if len(hm) > k:

                heappop(hm)

        return hm[0]


print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
