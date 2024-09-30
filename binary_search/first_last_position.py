# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Idea: here is to find the lower bound and then iterate from lower bound to find the index when we stop getting target element.


def searchRange(nums, target):

    def getLowerBound():

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if target <= nums[m]:
                r = m
            else:
                l = m + 1
        return l

    l = getLowerBound()
    res = -1

    for i in range(l, len(nums)):
        if nums[i] != target:
            break
        res = i

    return [l, res] if res != -1 else [-1, -1]
