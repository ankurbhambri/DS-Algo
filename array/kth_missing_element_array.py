# https://leetcode.com/problems/kth-missing-positive-number/

"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array.
"""


def findKthPositive(arr, k):
    l, r = 0, len(arr)

    while l < r:
        m = (l + r) // 2
        if arr[m] - (m + 1) < k:
            l = m + 1
        else:
            r = m
    return l + k


print(findKthPositive([2, 3, 4, 7, 11], 5))  # 9
print(findKthPositive([1, 2, 3, 4], 2))  # 6
