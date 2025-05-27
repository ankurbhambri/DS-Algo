# https://leetcode.com/problems/largest-divisible-subset/

def largestDivisibleSubset(nums):

    n = len(nums)
    nums.sort()
    res = [[num] for num in nums]
    
    for i in range(n):
        for j in range(i):
            if (nums[i] % nums[j]) == 0 and len(res[i]) < len(res[j]) + 1:
                res[i] = res[j] + [nums[i]]
                    
    return max(res, key=len)

print(largestDivisibleSubset([1, 2, 3])) # [1, 2]
print(largestDivisibleSubset([1, 2, 4, 8])) # [1, 2, 4, 8]
print(largestDivisibleSubset([3, 6, 7, 12])) # [3, 6, 12]
