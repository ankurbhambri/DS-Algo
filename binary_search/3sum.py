# https://leetcode.com/problems/3sum/


def threeSum(nums):

    nums.sort()
    n = len(nums)
    ans = set()

    for i in range(n):

        l, r = i + 1, n - 1
        remain = 0 - nums[i]

        while l < r:

            sum_val = nums[l] + nums[r]

            if sum_val == remain:
                ans.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1

            elif nums[l] + nums[r] > remain:
                r -= 1

            else:
                l += 1

    return list(ans)


print(threeSum([0, 1, 1]))  # []
print(threeSum([1, 1, 1, 0]))  # []
print(threeSum([0, 0, 0, 0]))  # [[0, 0, 0]]
print(threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
