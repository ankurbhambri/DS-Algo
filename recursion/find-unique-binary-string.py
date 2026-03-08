# https://leetcode.com/problems/find-unique-binary-string/


class Solution:
    def findDifferentBinaryString(self, nums):
        n = len(nums[0])
        nums = set(nums)

        def helper(val):

            if len(val) == n:
                if val not in nums:
                    return val
                else:
                    return ""

            return helper(val + "0") or helper(val + "1")

        return helper("")


# Cantor's Diagonal Argument (Approach)

class Solution:
    def findDifferentBinaryString(self, nums):

        ans = ""

        for i in range(len(nums)):

            # n ~ nums length and each element length will be ~ n also, nums[i].length == n
            curr = nums[i][i]

            # just opposing every value in nums
            ans += "1" if curr == "0" else "0"

        return ans