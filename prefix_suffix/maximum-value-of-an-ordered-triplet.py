# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/
# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

def maximumTripletValue(nums):

    n = len(nums)

    leftMax = [0] * n
    rightMax = [0] * n

    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], nums[i - 1])
        rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - i])

    res = 0
    for j in range(1, n - 1):
        res = max(res, (leftMax[j] - nums[j]) * rightMax[j])

    return res


print(maximumTripletValue([12,6,1,2,7])) # 77
print(maximumTripletValue([8,1,5,2,6])) # 42
