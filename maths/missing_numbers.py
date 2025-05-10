# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

def findDisappearedNumbers(nums):

    for num in nums:
        idx = abs(num) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]

    res = []
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)
    return res

print(findDisappearedNumbers([1,1]))  # Output: [2]
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # Output: [5, 6]