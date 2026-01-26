# https://leetcode.com/problems/kth-largest-element-in-an-array/

'''
Here, we are heap property, which ensure the root element is the smallest (min-heap) or largest (max-heap) element.
In python by default it is a min-heap, so we are making sure the size of heap is not exceeding k and keep popping the smallest element at the top (root).
The property of the heap is to maintain the order of elements, so that the smallest element is always at the root.
'''

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


print(Solution().findKthLargest([1], 1))  # 1
print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
print(Solution().findKthLargest([7, 6, 5, 4, 3, 2, 1], 5))  # 3
print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4


# Variant: What if we supposed to return the Kth+1 largest element?

class Solution:
    def findKthPlusOneLargest(self, nums, k: int) -> int:

        hm = []

        if k + 1 > len(nums):
            return None  # or appropriate value indicating not possible

        for i in nums:

            heappush(hm, i)

            if len(hm) > k + 1:

                heappop(hm)

        return hm[0]


# Variant: What if we supposed to return the Kth smallest element?

class Solution:
    def findKthSmallest(self, nums, k: int) -> int:

        hm = []

        for i in nums:

            heappush(hm, -i)  # pushing negative to simulate max-heap

            if len(hm) > k:

                heappop(hm)

        return -hm[0]  # return negative to get original value


print(Solution().findKthSmallest([1], 1))  # 1
print(Solution().findKthSmallest([3, 2, 1, 5, 6, 4], 2))  # 2
print(Solution().findKthSmallest([7, 6, 5, 4, 3, 2, 1], 5))  # 5
print(Solution().findKthSmallest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 3