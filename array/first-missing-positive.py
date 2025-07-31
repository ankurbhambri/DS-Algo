# https://leetcode.com/problems/first-missing-positive

# SC: O(N)

def firstMissingPositive(nums):
    
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

print(firstMissingPositive([1, 2, 0]))  # Output: 3
print(firstMissingPositive([3, 4, -1, 1]))  # Output: 2
