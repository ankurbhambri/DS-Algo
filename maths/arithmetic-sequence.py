
'''
An arithmetic sequence is a list of numbers with a definite pattern. If you take any number in the sequence then subtract it from the previous one, 
the difference is always a constant.

A good arithmetic sequence is an arithmetic sequence with a common difference of either 1 or -1.

For example, [4, 5, 6] is a good arithmetic sequence. Any sequence that has only one element is a good arithmetic sequence.

For example, [4] is a good arithmetic sequence.
Given an integer array nums, return the sum of the sums of each subarray that is a good arithmetic sequence.

Example:

Given nums = [7, 4, 5, 6, 5]. Each of the following subarrays is a good arithmetic sequence:

[7], [4], [5], [6], [5],
[4, 5], [5, 6], [6, 5],
[4, 5, 6]

The sums of these subarrays are:

7, 4, 5, 6, 5, = 27
4 + 5 = 9, 5 + 6 = 11, 6 + 5 = 11,
4 + 5 + 6 = 15

Thus, the answer is the sum of all the sums above, which is:

27 + 9 + 11 + 11 + 15 = 73.
'''

# A "good arithmetic sequence" is a subarray where every adjacent pair differs by
# a CONSTANT step of either +1 (ascending) or -1 (descending). Length-1 subarrays
# are always good.
#
# Idea (O(n) DP over subarrays ending at i):
#   For each i track, separately for the ascending and descending direction:
#     - count of good subarrays ending at i (including the single element [i])
#     - sum of the sums of those subarrays
#   Extending all chains ending at i-1 by nums[i] adds nums[i] once per chain.
#   Single elements are counted in BOTH directions, so subtract sum(nums) once.

# TC: O(n)
# SC: O(1)
class Solution:
    def sumOfGoodSubarrays(self, nums):

        total = 0

        # ascending (step +1) state
        # c_asc = count of good ascending subarrays ending at i
        # s_asc = sum of sums of good ascending subarrays ending at i
        c_asc = s_asc = 0

        # descending (step -1) state
        # c_desc = count of good descending subarrays ending at i
        # s_desc = sum of sums of good descending subarrays ending at i
        c_desc = s_desc = 0

        prev = None
        for x in nums:
            if prev and x - prev == 1:
                # extend every ascending chain ending at prev, plus the new single [x]
                s_asc = s_asc + x * c_asc + x
                c_asc += 1
            else:
                s_asc, c_asc = x, 1

            if prev and x - prev == -1:
                s_desc = s_desc + x * c_desc + x
                c_desc += 1
            else:
                s_desc, c_desc = x, 1

            # s_asc and s_desc both include the single element [x]; will fix below
            total += s_asc + s_desc
            prev = x

        # single elements were counted once in each direction -> remove one copy
        return total - sum(nums)


print(Solution().sumOfGoodSubarrays([7, 4, 5, 6, 5])) # 73
print(Solution().sumOfGoodSubarrays([7, 2, 3, 4])) # 37
