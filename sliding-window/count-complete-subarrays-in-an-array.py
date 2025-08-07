# https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/

'''
    You are given an array nums consisting of positive integers.

    We call a subarray of an array complete if the following condition is satisfied:

    The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
    Return the number of complete subarrays.

    A subarray is a contiguous non-empty part of an array.

    res += (n - r) .... intuition

        1. Ask yourself: “If I fix l, can I stretch r from here to the end and still keep the window valid?”

        If yes, use res += (n - r)

        If no, just do res += 1

'''

def countCompleteSubarrays(nums):

    l = 0
    res = 0
    freq = {}

    n = len(nums)
    k = len(set(nums))

    for r in range(n):

        freq[nums[r]] = 1 + freq.get(nums[r], 0)

        while len(freq) == k:
            # (n - r) gives the number of valid subarrays right to the current right pointer
            # as all elements in the current window are distinct and equal to k
            # so we can extend the right pointer to the end of the array
            # and all those subarrays will be valid.
            res += (n - r)

            freq[nums[l]] -= 1

            if freq[nums[l]] == 0:
                del freq[nums[l]]

            l += 1

    return res


print(countCompleteSubarrays([1,3,1,2,2]))  # Output: 4
print(countCompleteSubarrays([5,5,5,5]))  # Output: 10


# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description

# Question: Given an array of integers nums and an integer k, return the number of subarrays where the maximum element appears at least k times.

def countSubarrays(nums, k):

    l = 0
    res = 0
    freq = {}
    n = len(nums)
    max_ele = max(nums)

    for r in range(len(nums)):

        freq[nums[r]] = 1 + freq.get(nums[r], 0)

        while max_ele in freq and freq[max_ele] >= k:

            res += (n - r)  # Count all valid subarrays starting from l to r

            freq[nums[l]] -= 1

            if freq[nums[l]] == 0:
                del freq[nums[l]]

            l += 1

    return res

print(countSubarrays([1,3,2,3,3], 2))  # Output: 6
print(countSubarrays([1,4,2,1], 3))  # Output: 0
