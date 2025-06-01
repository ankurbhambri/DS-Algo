'''
    There are three similar sounding problems on internet, based on find duplicates, missing number.

    1. 442. Find All Duplicates in an Array (https://leetcode.com/problems/find-all-duplicates-in-an-array/)
    2. 41. First Missing Positive (https://leetcode.com/problems/first-missing-positive/)
    3. 287. Find the Duplicate Number (https://leetcode.com/problems/find-the-duplicate-number/)

    But they are different problems and there way of solving them is also different.

    Such as:
    - The first problem is solved using the negative marking technique,
    - Second problem is based on swaping the numbers to correct positions and then find if the number at index i is not i+1, that means missing number.
    - Third problem is solved using the slow and fast pointer technique, Floyd's Tortoise and Hare (Cycle Detection) algorithm. Which is also used to find the cycle in a linked list.

'''

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
