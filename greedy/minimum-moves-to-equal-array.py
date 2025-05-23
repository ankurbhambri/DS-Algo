# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

def minMoves(nums):
    """
    Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
    In one move, you can increment n - 1 elements by 1.
    """

    # The minimum number of moves is equal to the sum of differences between each element and the minimum element
    min_num = min(nums)
    moves = 0
    
    for num in nums:
        moves += num - min_num
    
    return moves

print(minMoves([1, 2, 3]))  # Output: 3
print(minMoves([1, 1, 1]))  # Output: 0


# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

def minMoves2(nums):

    nums.sort()
    n = len(nums)
    median = nums[n // 2]
    moves = 0
    
    for num in nums:
        moves += abs(num - median)
    
    return moves


# Example usage
nums = [1, 2, 3]
print(minMoves2(nums))  # Output: 2
nums = [1, 10, 2, 9]
print(minMoves2(nums))  # Output: 16
nums = [1, 2, 3, 4]
print(minMoves2(nums))  # Output: 4
