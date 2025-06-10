# https://leetcode.com/problems/split-array-largest-sum/


class Solution:
    def splitArray(self, nums, k):

        l = max(nums)            # smallest possible max subarray sum
        r = sum(nums)            # largest possible max subarray sum

        def helper(m):
            s = 1                # at least 1 subarray
            max_sm = 0           # running sum

            for n in nums:

                if max_sm + n <= m:
                    max_sm += n

                else:
                    max_sm = n   # start new subarray
                    s += 1       # count the split

            return s             # total number of subarrays formed

        while l < r:
            m = (l + r) // 2     # mid is candidate for max subarray sum
            s = helper(m)

            if s > k:
                l = m + 1        # too many splits → increase max allowed sum
            else:
                r = m            # try smaller max allowed sum

        return l                 # minimum max subarray sum possible
