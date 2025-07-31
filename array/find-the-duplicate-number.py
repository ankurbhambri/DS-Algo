# https://leetcode.com/problems/find-the-duplicate-number/description/


# Approach - Marking visited value within the array
# Idea: The idea is to use the fact that the numbers in the array are in the range from 1 to n, where n is the length of the array.
# We can use the indices of the array to mark the numbers we have seen by negating the value at the index corresponding to the number.
# If we encounter a number that has already been marked (i.e., the value at the index is negative), we know that this number is a duplicate.

# Time Complexity: O(n) where n is the length of the array.
# Space Complexity: O(1) since we are modifying the input array in place.

def findDuplicate(nums):

    n = len(nums)

    for num in nums:

        idx = abs(num)

        if nums[idx] < 0:
            return idx

        nums[idx] = -nums[idx]

    return n

print(findDuplicate([1, 3, 4, 2, 2]))  # Output: 2
print(findDuplicate([3, 1, 3, 4, 2])) # Output: 3
print(findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7])) # Output: 9
print(findDuplicate([1, 1]))  # Output: 1


# https://leetcode.com/problems/find-all-duplicates-in-an-array/

# Question is to find all duplicates in an array where each element is in the range from 1 to n (n is the length of the array).
# The approach is similar to the one used for finding a single duplicate, but we will collect all duplicates in a list.
# We will iterate through the array, and for each number, we will check if the value at the index corresponding to that number is negative.
# If it is negative, we have already seen this number, so we add it to the result list. If it is positive, we negate the value at that index to mark it as seen.
# Time Complexity: O(n) where n is the length of the array.
# Space Complexity: O(1) since we are modifying the input array in place and using a constant amount of extra space.

def findDuplicates(nums):

    res = []
    for num in nums:

        num = abs(num)

        if nums[num - 1] < 0:
            res.append(num)

        else:
            nums[num - 1] = -nums[num - 1]

    return res


print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])) # [2, 3]
print(findDuplicates([1, 1, 2])) # [1]
print(findDuplicates([1, 2, 3, 4, 5])) # []
print(findDuplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # []



# Another approach using Floyd's Tortoise and Hare (Cycle Detection)
# Idea: The idea is to treat the array as a linked list where each value points to the index of the next value.
# We can use two pointers, one moving at normal speed (tortoise) and the other moving at double speed (hare).
# If there is a cycle (which there will be since there is a duplicate), the two pointers will eventually meet.
# After finding the meeting point, we can reset one pointer to the start and move both pointers at the same speed until they meet again.
# This meeting point will be the duplicate number.

# Time Complexity: O(n) where n is the length of the array.
# Space Complexity: O(1) since we are using only a constant amount of extra space.


def findDuplicate(nums):

    # Step 1: Detect cycle
    tortoise = hare = nums[0] # fast and slow pointers
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


print(findDuplicate([1, 3, 4, 2, 2]))  # Output: 2
print(findDuplicate([3, 1, 3, 4, 2])) # Output: 3
print(findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7])) # Output: 9
print(findDuplicate([1, 1]))  # Output: 1
