# https://leetcode.com/problems/subsets/
# TC - O(N * S), SC - O(N)


def subsets(nums):
    res = [[]]

    for num in nums:
        # [[]] * [1], [[], [1]] * [2] ........
        res += [i + [num] for i in res]

    return res
