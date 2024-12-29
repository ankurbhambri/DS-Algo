# https://leetcode.com/problems/jump-game-ii/

# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
# Plus, return the path as well.


# O(n2)
def canReach(nums):

    n = len(nums)
    dp = [float("inf")] * n
    dp[-1] = 0

    for i in range(n - 2, -1, -1):

        if nums[i] != 0:

            for j in range(1, nums[i] + 1):

                if i + j < n:  # keeping the index in bound
                    dp[i] = min(dp[i], dp[i + j] + 1)

    # now we will find the shorsted path and print

    return dp[0]


# O(n)
def jump(nums):
    res = 0
    l = r = 0

    while r < len(nums) - 1:

        far = 0

        for i in range(l, r + 1):
            far = max(far, i + nums[i])

        l = r + 1
        r = far
        res += 1

    return res


# printing the path
def jump_path(nums):

    res = 0
    l = r = 0
    path = []

    while r < len(nums) - 1:
        far = 0
        next_index = -1

        for i in range(l, r + 1):
            if i + nums[i] > far:
                far = i + nums[i]
                next_index = i

        l = r + 1
        r = far
        path.append(next_index)
        res += 1

    path.append(len(nums) - 1)
    return res, path


print(canReach([3, 3, 0, 2, 1, 2, 4, 2, 0, 0]))
print(canReach([2, 3, 1, 1, 4]))
print(canReach([2, 3, 0, 1, 4]))


print(jump([3, 3, 0, 2, 1, 2, 4, 2, 0, 0]))
print(jump([2, 3, 1, 1, 4]))
print(jump([2, 3, 0, 1, 4]))


print(jump_path([3, 3, 0, 2, 1, 2, 4, 2, 0, 0]))
print(jump_path([2, 3, 1, 1, 4]))
print(jump_path([2, 3, 0, 1, 4]))
