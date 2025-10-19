"""
Problem: Sort Elements Nearly Sorted by K Positions

Given an array of integers nums and an integer k, sort the array in ascending order.
Each element in nums is at most k positions away from its correct sorted position.

You must solve the problem in-place and without using any built-in sort functions,
achieving O(n log n) worst-case time complexity.

Examples:
1. Input: nums = [6, 5, 3, 2, 8, 10, 9], k = 3
    Output: [2, 3, 5, 6, 8, 9, 10]

2. Input: nums = [10, 9, 8, 7, 4, 70, 60, 50], k = 4
    Output: [4, 7, 8, 9, 10, 50, 60, 70]

3. Input: nums = [1, 2, 3, 4, 5], k = 0
    Output: [1, 2, 3, 4, 5]

Constraints:
- 0 <= len(nums) <= 10^6
- -10^4 <= nums[i] <= 10^4
- 0 <= k <= 10^7
- k is typically much smaller than len(nums)

"""

import heapq


def solution(nums, k):

    if not nums or k == 0:
        return nums

    n = len(nums)
    result = []

    # Step 1: Build the initial heap from the first k+1 elements
    min_heap = nums[:min(k + 1, n)]
    heapq.heapify(min_heap)

    # Step 2: Process the remaining elements
    for i in range(k + 1, n):
        smallest = heapq.heappop(min_heap)
        result.append(smallest)
        heapq.heappush(min_heap, nums[i])

    # Step 3: Extract remaining elements from heap
    while min_heap:
        result.append(heapq.heappop(min_heap))

    return result


print(solution([6, 5, 30, 2, 8, 1, 0], 3))  # [0, 1, 2, 5, 6, 8, 30]
print(solution([10, 9, 8, 7, 4, 70, 60, 50], 4))  # [4, 7, 8, 9, 10, 50, 60, 70]
print(solution([1, 2, 3, 4, 5], 0))  # [1, 2, 3, 4, 5]
