# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
'''

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:

        l = 0
        res = 0
        zero = 0

        for i, n in enumerate(nums):

            # yha hum check karte h ki current element 0 h ya 1, agar 0 h to zero ko increment kar do
            # zero increment ka matlab ki humne ek 0 ko dekha or usse delete kar diya.
            if n == 0:
                zero += 1

            # ab hum check karenge ki kya humne 1 (delete limit) se zyada 0s dekhe,
            # agar haan to hum left pointer ko increment karenge jab tak ki zero <= 1 na ho jaye
            # aise karne se hum ensure karenge ki humari window mein sirf 1 ya 0 hi ho, aur 0 ka count 1 se zyada na ho.
            while zero > 1:

                if nums[l] == 0:

                    zero -= 1

                l += 1

            res = max(res, i - l)

        return res


print(Solution().longestSubarray([1, 1, 0, 1]))  # Output: 3
print(Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))  # Output: 5