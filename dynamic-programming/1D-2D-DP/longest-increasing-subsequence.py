# https://leetcode.com/problems/longest-increasing-subsequence/

# TC: O(n^2)
# SC: O(n)
def length_of_lis(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4
print(length_of_lis([0, 1, 0, 3, 2, 3]))  # Output: 4
print(length_of_lis([7, 7, 7, 7, 7, 7]))  # Output: 1
print(length_of_lis([]))  # Output: 0


# Print longest increasing subsequence
def printLengthOfLIS(nums):

    if not nums:
        return []

    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    lis = 0

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:

                dp[i] = dp[j] + 1

                prev[i] = j # Store the previous index, that was smaller

                lis = i if dp[lis] < dp[i] else lis # keep track of the longest increasing subsequence length

    res = []
    while lis > -1: # Backtrack to find the longest increasing subsequence
        res.append(nums[lis])
        lis = prev[lis]
    
    res.reverse() # Reverse the result to get the correct order
    return res

print(printLengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: [2, 3, 7, 101]
print(printLengthOfLIS([0, 1, 0, 3, 2, 3]))  # Output: [0, 1, 2, 3]
print(printLengthOfLIS([7, 7, 7, 7, 7, 7]))  # Output: [7]
print(printLengthOfLIS([]))  # Output: []

# Similar question - https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii

# Approach 2: Binary Search (O(n log n))

import bisect

def LIS(arr):
    sub = []
    for x in arr:
        # binary search position
        pos = bisect.bisect_left(sub, x)
        if pos == len(sub):
            sub.append(x)
        else:
            sub[pos] = x
    return len(sub)

print(LIS([10,9,2,5,3,7,101,18]))  # Output: 4
