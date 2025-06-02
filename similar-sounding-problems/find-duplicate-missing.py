'''
    There are five similar sounding problems on the internet, based on finding duplicates or missing numbers:

    1. 268. Missing Number (https://leetcode.com/problems/missing-number/)
    2. 442. Find All Duplicates in an Array (https://leetcode.com/problems/find-all-duplicates-in-an-array/)
    3. 41. First Missing Positive (https://leetcode.com/problems/first-missing-positive/)
    4. 448. Find All Numbers Disappeared in an Array (https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)
    5. 287. Find the Duplicate Number (https://leetcode.com/problems/find-the-duplicate-number/)

    Although they sound similar, they are distinct problems with different approaches to solving them.

    For example:
    - The first problem is solved using Gauss' formula to calculate the expected sum and subtracting the actual sum.
    - The second problem uses the negative marking technique to identify duplicates.
    - The third problem involves swapping numbers to their correct positions and then checking for the first missing positive integer.
    - The fourth problem uses negative marking to identify missing numbers.
    - The fifth problem is solved using Floyd's Tortoise and Hare (Cycle Detection) algorithm, which is also used to detect cycles in linked lists.
'''

# https://leetcode.com/problems/missing-number/

# Gauss' Formula
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        sm = sum(nums)
        t = (n * (n + 1 ) ) // 2
        return t - sm

print(Solution().missingNumber([3, 0, 1]))  # Output: 2


# https://leetcode.com/problems/find-all-duplicates-in-an-array/

# Here, we are using the negative marking technique to find duplicates.
class Solution:
    def findDuplicates(self, nums):
        res = []
        for i in nums:
            num = abs(i)
            if nums[num - 1] < 0:
                res.append(num)
            else:
                nums[num - 1] = -nums[num - 1]
        return res

print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # Output: [2, 3]


# https://leetcode.com/problems/first-missing-positive/

# This problem is solved by placing each number in its correct position if possible, and then checking for the first missing positive integer.
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Step 1: Place each number in its correct position if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # Step 2: Find the first index where nums[i] != i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positions are filled correctly, return n + 1
        return n + 1

print(Solution().firstMissingPositive([3, 4, -1, 1]))  # Output: 2


# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums):

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res
    
print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # Output: [5, 6]


# https://leetcode.com/problems/find-the-duplicate-number/

# This problem is solved using the Floyd's Tortoise and Hare (Cycle Detection) algorithm.
class Solution:
    def findDuplicate(self, nums):

        # Step 1: Detect cycle
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Step 2: Find the entrance to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare

print(Solution().findDuplicate([1, 3, 4, 2, 2]))  # Output: 2
print(Solution().findDuplicate([3, 1, 3, 4, 2]))  # Output: 3
