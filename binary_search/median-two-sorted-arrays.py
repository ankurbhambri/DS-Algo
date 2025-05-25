# Task is to find the median of two sorted arrays


# Aproach 1: space efficient brute force
# Time complexity: O(n + m)
# Space complexity: O(1)

def findMedianSortedArrays(nums1, nums2):

    n, m = len(nums1), len(nums2)
    i, j = 0, 0
    size = m + n # total size of merged array

    idx1 = (size // 2) - 1
    ele1 = -1
    idx2 = (size // 2)
    ele2 = -1

    k = 0
    while i < n and j < m:
        if nums1[i] < nums2[j]:
            if k == idx1:
                ele1 = nums1[i]
            if k == idx2:
                ele2 = nums1[i]
            i += 1
        else:
            if k == idx1:
                ele1 = nums2[j]
            if k == idx2:
                ele2 = nums2[j]
            j += 1
        k += 1

    while i < n:
        if k == idx1:
            ele1 = nums1[i]
        if k == idx2:
            ele2 = nums1[i]            
        i += 1
        k += 1
    while j < m:
        if k == idx1:
            ele1 = nums2[j]
        if k == idx2:
            ele2 = nums2[j]
        j += 1
        k += 1

    if size % 2 == 1:
        return ele2

    return (ele1 + ele2) / 2


# Approach 2: Binary search
# Time complexity: O(log(min(n, m)))
# Space complexity: O(1)


def findMedianSortedArrays(nums1, nums2):

    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)  # Ensure nums1 is smaller
    
    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)

        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1


print(findMedianSortedArrays([1, 3, 8], [7, 9, 10, 11]))  # Output: 8
print(findMedianSortedArrays([1, 3, 5], [2, 4, 6]))  # Output: 3.5
