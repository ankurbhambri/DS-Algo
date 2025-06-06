# https://leetcode.com/problems/3sum-closest/description/

'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''


def threeSumClosest(nums, target):

    dist = float("inf")
    nums.sort()

    for i in range(len(nums)):

        l, r = i + 1, len(nums) - 1
        remain = target - nums[i]

        while l < r:

            sum_val = nums[l] + nums[r]

            if sum_val == remain:
                return target  # return target

            if abs(dist) > abs(remain - sum_val):  # closest value
                dist = remain - sum_val

            elif sum_val > remain:
                r -= 1
            else:
                l += 1

    return target - dist


print(threeSumClosest([-1, 2, 1, -4], 1))  # 2
print(threeSumClosest([1, 1, 1, 0], -100))  # 2
print(threeSumClosest([1, 1, 1, 0], 100))  # 3
print(threeSumClosest([1, 1, 1, 0], 0))  # 2
