def getMaxLen(nums):

    res = 0
    neg_count = 0
    early_zero = -1
    early_neg = None

    for i in range(len(nums)):

        if nums[i] < 0:
            if early_neg is None:
                early_neg = i
            neg_count += 1
        
        elif nums[i] == 0:
            early_neg = None
            early_zero = i
            neg_count = 0

        if neg_count % 2 == 1:
            res = max(res, i - early_neg)
        else:
            res = max(res, i - early_zero)

    return res


print(getMaxLen([-1]))  # Output: 0
print(getMaxLen([-1,2]))  # Output: 1
print(getMaxLen([1,-2,-3,4]))  # Output: 4
print(getMaxLen([0,1,-2,-3,-4]))  # Output: 3
print(getMaxLen([-1,-2,-3,0,1]))  # Output: 2
