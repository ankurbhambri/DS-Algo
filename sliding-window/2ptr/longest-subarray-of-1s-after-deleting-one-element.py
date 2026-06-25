class Solution:
    def longestSubarray(self, nums: list[int]) -> int:

        l = 0
        one = 0
        res = 0

        for i, n in enumerate(nums):

            if n == 0:
                one += 1

            while one > 1:

                if nums[l] == 0:

                    one -= 1

                l += 1

            res = max(res, i - l)

        return res
