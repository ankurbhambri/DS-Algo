# https://leetcode.com/problems/find-peak-element/

def findPeakElement(nums):

    l, r = 0, len(nums) - 1

    while l < r:

        m = l + (r - l) // 2

        if nums[m] < nums[m + 1]:
            l = m + 1

        else:
            r = m

    return l

print(findPeakElement([1, 2, 3, 1]))
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print(findPeakElement([1, 2, 3, 4, 5]))
print(findPeakElement([5, 4, 3, 2, 1]))

# VARIANT: What if you had to find the valley element, no longer a peak element?

def findValleyElement(nums):

    l, r = 0, len(nums) - 1

    while l < r:

        m = l + (r - l) // 2

        if nums[m] > nums[m + 1]:
            l = m + 1

        else:
            r = m

    return l

print(findValleyElement([1, 2, 3, 1]))
print(findValleyElement([3, 2, 1, 2, 3]))
print(findValleyElement([6, 5, 4, 3, 2, 3, 4]))
print(findValleyElement([5, 4, 3, 2, 1]))
print(findValleyElement([1, 2, 3, 4, 5]))