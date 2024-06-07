# https://leetcode.com/problems/longest-consecutive-sequence/description/


def longestConsecutive(arr):
    arr = set(arr)
    res = 0
    for i in arr:
        if i - 1 not in arr:
            c = 0
            while i + c in arr:
                c += 1
            res = max(res, c)
    return res


print(longestConsecutive([100, 4, 0, 200, 2, 3, 1]))  # Output: 4
