# https://leetcode.com/problems/single-element-in-a-sorted-array/

# TC: O(n)
# SC: O(1)

# XOR Approach: Here equal numbers cancel each other out, leaving only the single number.
def singleNonDuplicate(nums):
    a = 0
    for i in nums:
        a ^= i
    return a

print(singleNonDuplicate([1]))
print(singleNonDuplicate([2, 2, 1]))
print(singleNonDuplicate([4, 1, 2, 1, 2]))
print(singleNonDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(singleNonDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



# TC: O(log n)
# SC: O(1)

# Binary Search Approach

'''
    The key observation:

        Before the single element, the first of each pair is at even index.

        After the single element, the first of each pair is at odd index (because the sequence is shifted).

        We are ensuring that mid is even so that we can always compare the pair: nums[mid] and nums[mid + 1]. This allows us to treat the array as pairs starting at even indices.

        We can reason cleanly:

            If nums[mid] == nums[mid + 1] → the pair is valid → go right

            Else → the single must be at mid or to the left
'''

class Solution:
    def singleNonDuplicate(self, nums):

        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2

            # Ensure mid is even for easier comparison
            if m % 2 == 1:
                m -= 1

            # If pair is on the left, single is on the right
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                r = m

        # Left will point to the single element
        return nums[l]


print(Solution().singleNonDuplicate([1]))
print(Solution().singleNonDuplicate([2, 2, 1]))
print(Solution().singleNonDuplicate([4, 1, 2, 1, 2]))
print(Solution().singleNonDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(Solution().singleNonDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))