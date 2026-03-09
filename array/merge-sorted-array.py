# https://leetcode.com/problems/merge-sorted-array/description/

'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.

To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


Constraints:

    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109
'''

class Solution:
    def merge(self, nums1, m, nums2, n):

        last = len(nums1) - 1
        
        while m > 0 and n > 0:

            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1

            last -= 1

        while n > 0:

            nums1[last] = nums2[n - 1]

            n -= 1
            last -= 1
            
        return nums1

print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))  # [1,2,2,3,5,6]
print(Solution().merge([1], 1, [], 0))  # [1]
print(Solution().merge([0], 0, [1], 1))  # [1]


# VARIANT: What if the sizes - m and n - weren't given? Instead, we're guaranteed that one list is double in size of the other. 
# Merge them like you would in the original problem.

class Solution:
    def mergeWithoutSizes(self, nums1, nums2):

        m = len(nums1) // 2
        n = len(nums2)

        last = len(nums1) - 1
        
        while m > 0 and n > 0:

            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1

            last -= 1

        while n > 0:

            nums1[last] = nums2[n - 1]

            n -= 1
            last -= 1
            
        return nums1

print(Solution().mergeWithoutSizes([1,2,3,0,0,0], [2,5,6]))  # [1,2,2,3,5,6]
print(Solution().mergeWithoutSizes([1], []))  # [1]
print(Solution().mergeWithoutSizes([0], [1]))  # [1]