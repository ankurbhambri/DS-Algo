# https://leetcode.com/problems/count-subarrays-with-fixed-bounds

'''
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

'''

def countSubarrays(nums, minK: int, maxK: int):
    res = 0
    bad_idx = -1  # Last invalid element index
    min_idx = -1  # Last minK index
    max_idx = -1  # Last maxK index
    
    # Iterate over nums, for each number at index i:
    for i in range(len(nums)):

        # If the number is outside the range [minK, maxK], update the most recent left_bound.
        if nums[i] < minK or nums[i] > maxK:
            bad_idx = i

        # if element is minK
        if nums[i] == minK:
            min_idx = i

        # if element is maxK
        if nums[i] == maxK:
            max_idx = i
            
        # The number of valid subarrays equals the number of elements between left_bound and 
        # the smaller of the two most recent positions.
        start = min(min_idx, max_idx)
        if start > bad_idx:
            res += start - bad_idx

    return res


print(countSubarrays([1, 3, 5, 2, 7, 5], 1, 5))  # Output: 2
print(countSubarrays([1, 3, 5, 2, 7, 5], 1, 7))  # Output: 2
print(countSubarrays([1, 3, 5, 2, 7, 5], 2, 5))  # Output: 2
print(countSubarrays([1, 3, 5, 2, 7, 5], 3, 5))  # Output: 1
