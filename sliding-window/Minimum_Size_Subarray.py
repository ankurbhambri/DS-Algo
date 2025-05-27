# https://leetcode.com/problems/minimum-size-subarray-sum/


def minSubArrayLen(target, nums):

    l, total = 0, 0
    res = float("inf")

    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(res, r - l + 1)
            total -= nums[l]
            l += 1

    return 0 if res == float("inf") else res


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2
print(minSubArrayLen(4, [1, 4, 4]))  # 1
print(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # 0
print(minSubArrayLen(11, [1, 2, 3, 4, 5]))  # 3
print(minSubArrayLen(15, [1, 2, 3, 4, 5]))  # 5
print(minSubArrayLen(100, [1, 2, 3, 4, 5]))  # 0
