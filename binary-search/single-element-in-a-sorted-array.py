# https://leetcode.com/problems/single-element-in-a-sorted-array/

def singleNonDuplicate(nums):
    a = 0
    for i in nums:
        a ^= i
    return a

print(singleNonDuplicate([2, 2, 1]))
print(singleNonDuplicate([4, 1, 2, 1, 2]))
print(singleNonDuplicate([1]))
print(singleNonDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(singleNonDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# Binary Search Approach

def singleNonDuplicate(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        # Make sure mid points to the first element of a pair
        if mid % 2 == 1:
            mid -= 1
        # Check if mid and mid+1 form a pair
        if nums[mid] == nums[mid + 1]:
            # Single element is in right half
            left = mid + 2
        else:
            # Single element is in left half or at mid
            right = mid
    
    return nums[left]