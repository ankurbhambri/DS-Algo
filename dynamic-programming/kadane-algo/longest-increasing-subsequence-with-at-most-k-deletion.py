'''
Given a number array of length n and a number k, what is the longest non-decreasing contiguous subarray if we allow at most k deletions in our original array?

example: n, k = 5, 2 array = 5 2 1 3 4

answer = 2 3 4 with deleting 1 from index 2.

https://math.stackexchange.com/questions/3953797/longest-increasing-subsequence-with-at-most-k-deletion

'''

import bisect

# TC: O(n log n)
# SC: O(n)

def longest_increasing_subsequence_with_k_deletions(nums, K):
    n = len(nums)
    
    # dp[i] = the smallest possible tail value of an increasing subsequence of length i+1
    dp = []

    for num in nums:
        idx = bisect.bisect_left(dp, num)
        if idx == len(dp):
            dp.append(num)
        else:
            dp[idx] = num
    
    lis_len = len(dp)

    # We need LIS such that n - LIS_len <= K → LIS_len >= n - K
    if n - lis_len <= K:
        return lis_len

    return n - K

print(longest_increasing_subsequence_with_k_deletions([3, 2, 5, 1, 7], 1))  # Output: 4
print(longest_increasing_subsequence_with_k_deletions([1, 2, 3, 4, 5], 2))  # Output: 5
