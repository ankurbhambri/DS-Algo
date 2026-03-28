# https://leetcode.com/problems/buildings-with-an-ocean-view


def func(arr):

    if not arr:
        return []

    max_height = float("-inf")
    res = []

    for i in range(len(arr) - 1, -1, -1):

        if arr[i] > max_height:
            res.append(i)
            max_height = arr[i]

    return res[::-1]


print(func([4, 2, 3, 1]))
