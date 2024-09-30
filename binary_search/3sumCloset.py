def threeSumClosest(nums, target):

    dist = float("inf")
    nums.sort()

    for i in range(len(nums) - 2):

        remain = target - nums[i]
        l, r = i + 1, len(nums) - 1

        while l < r:

            sum_val = nums[l] + nums[r]
            if sum_val == remain:
                return target

            if abs(dist) > abs(remain - sum_val):
                dist = remain - sum_val

            if sum_val < remain:
                l += 1
            else:
                r -= 1

    return target - dist


print(threeSumClosest([-1, 2, 1, -4], 1))  # 2
print(threeSumClosest([1, 1, 1, 0], -100))  # 2
print(threeSumClosest([1, 1, 1, 0], 100))  # 3
print(threeSumClosest([1, 1, 1, 0], 0))  # 2
