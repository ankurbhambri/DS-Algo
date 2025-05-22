# https://leetcode.com/problems/find-all-duplicates-in-an-array/

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
