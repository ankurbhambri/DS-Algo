# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Idea: here is to find the lower bound and then iterate from lower bound to find the index when we stop getting target element.


def searchRange(nums, target):

    def lowerBound():

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if target <= nums[m]:
                r = m
            else:
                l = m + 1
        return l

    l = lowerBound()
    res = -1

    for i in range(l, len(nums)):
        if nums[i] != target:
            break
        res = i

    return [l, res] if res != -1 else [-1, -1]


print(searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
print(searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
print(searchRange([5, 7, 7, 8, 8, 10], 7))  # [1, 2]
print(searchRange([5, 7, 7, 8, 8, 10], 5))  # [0, 0]
print(searchRange([5, 7, 7, 8, 8, 10], 10))  # [5, 5]
print(searchRange([5, 7, 7, 8, 8, 10], 11))  # [-1, -1]
print(searchRange([5, 7, 7, 8, 8, 10], 4))  # [-1, -1]
print(searchRange([], 0))  # [-1, -1]
print(searchRange([1], 1))  # [0, 0]
print(searchRange([1], 2))  # [-1, -1]
