# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

from math import ceil


def smallestDivisor(nums, threshold):
    l, r = 1, max(nums)

    def helper(m):
        x = 0
        for n in nums:
            x += ceil(n / m)
        return x

    while l < r:

        m = (l + r) // 2
        x = helper(m)

        if x <= threshold:
            r = m
        else:
            l = m + 1

    return l


print(smallestDivisor([19], 5))  # 4
print(smallestDivisor([1, 2, 3], 6))  # 1
print(smallestDivisor([1, 2, 5, 9], 6))  # 5
print(smallestDivisor([2, 3, 5, 7, 11], 11))  # 3
print(smallestDivisor([962551, 933661, 905225, 923035, 990560], 10))  # 495280
