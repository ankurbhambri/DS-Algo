# https://leetcode.com/problems/4sum/


'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.

nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

'''

def fourSum(nums, target):

    nums.sort()
    n = len(nums)
    ans = set()

    for i in range(n):
        for j in range(i + 1, n):

            l, r = j + 1, n - 1
            remain = target - nums[i] - nums[j]

            while l < r:

                if nums[l] + nums[r] == remain:
                    ans.add((nums[i], nums[j], nums[l], nums[r]))
                    l += 1
                    r -= 1

                elif nums[l] + nums[r] > remain:
                    r -= 1

                else:
                    l += 1
    return ans


target = 0
nums = [1, 0, -1, 0, -2, 2]
print(fourSum(nums, target))
