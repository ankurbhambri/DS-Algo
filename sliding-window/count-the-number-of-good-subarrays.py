# https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

'''
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.
'''

from collections import defaultdict

def countGood(nums, k):    

    freq = {}
    l = 0
    pair_count = 0
    result = 0
    n = len(nums)

    for r in range(n):

        # Add nums[r] to the window
        pair_count += freq.get(nums[r], 0)

        freq[nums[r]] = 1 + freq.get(nums[r], 0)

        # Shrink window from the left if we have enough pairs
        while pair_count >= k:

            # At this point, we have at least k pairs in the window, and if we add more value in the window it will increase the number of subarray counts
            result += n - r  # So, thats why we are considering the remaining elements as subarray, including the current subarry

            freq[nums[l]] -= 1

            pair_count -= freq[nums[l]]

            l += 1

    return result


print(countGood([1,1,1,1,1], 10)) # Output: 1
print(countGood([3,1,4,3,2,2,4], 2)) # Output: 4
