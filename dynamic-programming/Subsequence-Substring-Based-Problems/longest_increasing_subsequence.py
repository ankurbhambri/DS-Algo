# https://leetcode.com/problems/longest-increasing-subsequence/

"""
    The idea here is to use dynamic programming to solve the problem.
    We start with a dp array of length equal to the number of elements in the input array, nums.
    We initialize each element of the dp array to 1, as the minimum length of any subsequence is 1.

    Then, we iterate over the elements of the nums array.
    For each element, we iterate over the previous elements (from 0 to i-1) and check if the current element is greater than the previous element.
    If it is, we update the dp array at index i with the maximum value between its current value and 1 plus the dp value at the previous index.
    This ensures that we keep track of the longest increasing subsequence ending at each index.

    Finally, we return the maximum value in the dp array, which represents the length of the longest increasing subsequence in the nums array.

    TC: O(n^2)
    SC: O(n)
"""


def lengthOfLIS(nums):
    dp = [1] * len(nums)

    for i in range(1, len(nums)):  # -> i to len(nums)
        for j in range(i):  # -> 0 to i
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)


print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
print(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # 1
print(lengthOfLIS([4, 10, 4, 3, 8, 9]))  # 3
print(lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))  # 6

import bisect

"""
    The idea here is to use binary search to solve the problem.
    We start with an empty list, sub, which will store the smallest tail of all increasing subsequences of different lengths.

    For each element in the input array, we perform a binary search on the sub list to find the index where the current element can be placed.
    If the index is equal to the length of the sub list, it means that the current element is greater than all elements in sub, so we append it to sub.
    Otherwise, we replace the element at that index with the current element.

    Finally, we return the length of the sub list, which represents the length of the longest increasing subsequence in the nums array.

    TC: O(n log n)
    SC: O(n)
"""

def lengthOfLIS(nums):
    sub = []

    for num in nums:
        i = bisect.bisect_left(sub, num)  # binary search
        if i == len(sub):
            sub.append(num)  # extend the LIS
        else:
            sub[i] = num  # replace with smaller value to allow more future extensions

    return len(sub)


print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
print(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # 1
print(lengthOfLIS([4, 10, 4, 3, 8, 9]))  # 3
print(lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))  # 6
