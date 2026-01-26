# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums, target):

        if not nums:
            return [-1, -1]

        # Helper function to find the lower and upper bounds        
        def helper(logic):

            l, r = 0, len(nums)

            while l < r:

                m = (l + r) // 2

                if logic(nums[m], target):
                    l = m + 1

                else:
                    r = m

            return l

        lower_bound = helper(lambda a, b: a < b)
        upper_bound = helper(lambda a, b: a <= b)

        # Validate target is actually in the range
        if lower_bound == len(nums) or nums[lower_bound] != target:
            return [-1, -1]

        return [lower_bound, upper_bound - 1]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
print(Solution().searchRange([], 0))  # [-1, -1]
print(Solution().searchRange([1], 1))  # [0, 0]
print(Solution().searchRange([1, 2, 3, 4, 5], 3))  # [2, 2]


# Variant: What if we had to return the count of an element? (Yes, we still have to use binary search)

def countOccurrences(nums, target):

    if not nums:
        return 0

    def helper(logic):

        l, r = 0, len(nums)

        while l < r:

            m = (l + r) // 2

            if logic(nums[m], target):
                l = m + 1

            else:
                r = m

        return l

    lower_bound = helper(lambda a, b: a < b)
    upper_bound = helper(lambda a, b: a <= b)

    if lower_bound == len(nums) or nums[lower_bound] != target:
        return 0

    return upper_bound - lower_bound


print(countOccurrences([5, 7, 7, 8, 8, 10], 8))  # 2
print(countOccurrences([5, 7, 7, 8, 8, 10], 6))  # 0
print(countOccurrences([], 0))  # 0
print(countOccurrences([1], 1))  # 1
print(countOccurrences([1, 2, 2, 2, 3, 4, 5], 2))  # 3


# Variant: What if we had to return the count of unique elements in array?

# for example: [1,1,2,2,3,4,4] -> 4 (1,2,3,4) unique elements

# TC: O(K log N) # K = number of unique elements
# SC: O(1)

def countUniqueElements(nums):

    if not nums:
        return 0

    i = 0
    res = 0
    n = len(nums)

    while i < n:

        l = i
        r = n - 1

        target = nums[i]

        while l <= r:

            m = (l + r) // 2

            if nums[m] == target:
                l = m + 1

            else:
                r = m - 1

        res += 1
        i = r + 1
    
    return res

print(countUniqueElements([]))  # 0
print(countUniqueElements([1, 1, 1, 1, 1]))  # 1
print(countUniqueElements([1, 2, 3, 4, 5]))  # 5
print(countUniqueElements([5, 7, 7, 8, 8, 10]))  # 4