def findDuplicates(nums):
    res = []
    for num in nums:
        num = abs(num)
        if nums[num - 1] < 0:
            res.append(num)
        else:
            nums[num - 1] = -nums[num - 1]
    return res


print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3])
