# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

from heapq import heappush, heappop


class Solution:
    def k_smallest_pairs(self, nums1, nums2, k):

        if not nums1 or not nums2 or k <= 0:
            return []

        min_heap = []
        result = []

        # Only push the first k pairs from nums1 with nums2[0]
        for i in range(min(k, len(nums1))):
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        while min_heap and len(result) < k:

            _, i, j = heappop(min_heap)

            result.append((nums1[i], nums2[j]))

            if j + 1 < len(nums2):
                # Push next element in nums2 with current nums1[i]
                heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result    


print(Solution().kSmallestPairs([1, 2], [3], 3))  # [[1, 3], [2, 3]]
print(Solution().kSmallestPairs([1, 7], [3, 4], 2))  # [[1, 3], [1, 4]]
print(Solution().kSmallestPairs([1, 1, 2], [1, 2, 3], 3))  # [[1, 1], [1, 2], [1, 3]]
print(Solution().kSmallestPairs([1, 2, 3], [4, 5, 6], 4))  # [[1, 4], [1, 5], [2, 4], [2, 5]]
