# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def findMin(nums):

    l, r = 0, len(nums) - 1

    while l < r:
        m = l + (r - l) // 2

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m

    return nums[l]


print(findMin([3, 4, 5, 1, 2]))
print(findMin([4, 5, 6, 7, 0, 1, 2]))
print(findMin([3,1,2]))
print(findMin([2, 3, 4, 5, 6, 7, 8, 9, 10]))
