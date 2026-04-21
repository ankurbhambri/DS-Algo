# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

from math import ceil


def minimumSize(nums, maxOperations):


    def helper(m):

        t_ops = 0

        for n in nums:
            t_ops += ceil(n / m) - 1

        return t_ops

    l, r = 1, max(nums) # here, we can start with 1 as the minimum possible size of a bag, and max(nums) as the maximum possible size of a bag (since we can't have a bag larger than the largest number of balls in any bag).

    while l < r:

        m = (l + r) // 2

        t_ops = helper(m)

        if t_ops > maxOperations:
            l = m + 1
        else:
            r = m

    return l