# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq


def findKthLargest(nums, k):
    minhp = []
    for i in nums:
        heapq.heappush(minhp, i)
        if len(minhp) > k:
            heapq.heappop(minhp)
    return minhp[0]


print(findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
