# https://leetcode.com/problems/intersection-of-two-arrays/description/

from collections import Counter


class Solution(object):
    def intersection(self, nums1, nums2):

        # Initialize seen dictionary and res array
        seen = {}
        result = []

        # mark values occurring in nums1
        for x in nums1:
            seen[x] = 1

        for x in nums2:
            # Check if x is in the dictionary and not in the result (while checking if it is seen only once)
            if x in seen and seen[x] == 1:
                result.append(x)
                seen[x] = 0

        # Return the result
        return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(Solution().intersection(nums1, nums2))  # [2,2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(Solution().intersection(nums1, nums2))  # [4,9] or [9,4] both correct
