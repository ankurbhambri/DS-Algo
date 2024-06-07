# https://leetcode.com/problems/summary-ranges/

# https://leetcode.com/discuss/interview-question/1007960/bloomberg-phone-find-all-ranges-of-consecutive-numbers-from-array


def summaryRanges(nums):
    res = []
    for i in nums:
        # checking previous element is equal to current element - 1
        if res and res[-1][1] == i - 1:
            res[-1][1] = i
        else:
            res.append([i, i])

    return [str(x) + "->" + str(y) if x != y else str(x) for x, y in res]


print(summaryRanges([0, 1, 2, 4, 5, 7]))
print(summaryRanges([1, 2, 3, 4, 6, 8, 9]))
