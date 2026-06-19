'''
An arithmetic sequence is a list of numbers with a definite pattern. If you take any number in the sequence then subtract it from the previous one, the difference is always a constant.

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

7, 4, 5, 6, 5,
4 + 5 = 9, 5 + 6 = 11, 6 + 5 = 11,
4 + 5 + 6 = 15

Thus, the answer is the sum of all the sums above, which is:

7 + 4 + 5 + 6 + 5 + 9 + 11 + 11 + 15 = 73.
'''

class Solution:
    def goodArithmeticSum(self, nums):
        n = len(nums)
        ans = 0
        i = 0

        while i < n:

            j = i

            # extend segment while diff is ±1
            while j + 1 < n and abs(nums[j + 1] - nums[j]) == 1:
                j += 1

            # process segment [i, j]
            for k in range(i, j + 1):
                left = k - i + 1
                right = j - k + 1
                ans += nums[k] * left * right

            i = j + 1

        return ans

print(Solution().goodArithmeticSum([7, 4, 5, 6, 5]))  # Output: 73