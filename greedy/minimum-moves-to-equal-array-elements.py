# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/

# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

def minMoves2(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(x - median) for x in nums)

print(minMoves2([1, 2, 3]))  # Output: 2
print(minMoves2([1, 10, 2, 9]))  # Output: 16

