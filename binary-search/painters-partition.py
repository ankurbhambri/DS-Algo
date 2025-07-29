# https://leetcode.com/problems/split-array-largest-sum/description/
# https://www.naukri.com/code360/problems/painter-s-partition-problem_1089557
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

# Given the 

def splitArray(nums, k):

    l = max(nums)
    r = sum(nums)

    def helper(m):
        s = 1
        max_sm = 0
        for n in nums:
            if max_sm + n <= m:
                max_sm += n
            else:
                max_sm = n
                s += 1
        return s

    while l < r:
        m = (l + r) // 2

        s = helper(m)

        if s > k:
            l = m + 1
        else:
            r = m

    return l


print(splitArray([7, 2, 5, 10, 8], 2))  # 18
print(splitArray([1, 2, 3, 4, 5], 2))  # 9

# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

from math import ceil


def minimumSize(nums, maxOperations):
    l, r = 1, max(nums)

    def helper(m):
        t_ops = 0
        for n in nums:
            t_ops += ceil(n / m) - 1
        return t_ops

    while l < r:
        m = (l + r) // 2
        t_ops = helper(m)
        if t_ops > maxOperations:
            l = m + 1
        else:
            r = m
    return l
