from collections import Counter

# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/


# O(nlogn) solution


def get_first_greater_or_equal(nums, val):
    start = 0
    end = len(nums) - 1

    index = len(nums)
    while start <= end:
        mid = (start + end) // 2

        if nums[mid] >= val:
            index = mid
            end = mid - 1
        else:
            start = mid + 1

    return index


def solution(nums):
    nums.sort()

    N = len(nums)
    for i in range(1, N + 1):
        k = get_first_greater_or_equal(nums, i)

        if N - k == i:
            return i


# O(n) solution
def specialArray(nums):
    count, nums = 0, Counter(nums)
    for i in range(max(nums), -1, -1):
        count += nums[i]
        if count == i:
            return count
    return -1


# 3 must be the answer because 3 elements are greater than or equal to 3 in the array
print(specialArray([3, 5]))
print(solution([1, 2, 4, 5, 6]))
print(specialArray([1, 2, 4, 5, 6]))
