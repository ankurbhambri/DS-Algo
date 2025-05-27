# https://leetcode.com/problems/single-number/

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. Solve in linear complexity


def singleNumber(nums):
    a = 0
    for i in nums:
        a ^= i
    return a


print(singleNumber([4, 1, 2, 1, 2]))
