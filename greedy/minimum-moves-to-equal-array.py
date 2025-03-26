def minMoves(nums):

    nums.sort()
    n = len(nums)
    median = nums[n // 2]
    moves = 0
    
    for num in nums:
        moves += abs(num - median)
    
    return moves


# Example usage
nums = [1, 2, 3]
print(minMoves(nums))  # Output: 2
nums = [1, 10, 2, 9]
print(minMoves(nums))  # Output: 16
nums = [1, 2, 3, 4]
print(minMoves(nums))  # Output: 4
