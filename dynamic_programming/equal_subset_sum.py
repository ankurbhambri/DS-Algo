# https://leetcode.com/problems/partition-equal-subset-sum/description/


def equal_sum_recursive(arr):

    if sum(arr) % 2 != 0:
        return False

    def helper(i, W):

        # Base Cases
        if W == 0:
            return True

        elif i == 0:
            return False

        else:
            item = arr[i - 1]
            if item <= W:
                c1 = helper(i - 1, W - item)
                c2 = helper(i - 1, W)
                return c1 or c2
            else:
                return helper(i - 1, W)

    return helper(len(arr), sum(arr) // 2)


def equal_sum_memo(nums):

    if sum(nums) % 2 != 0:
        return False

    dp = set()
    dp.add(0)

    val = sum(nums) // 2

    for i in range(len(nums) - 1, -1, -1):
        nextDp = set()
        for t in dp:
            nextDp.add(t + nums[i])
            nextDp.add(t)

        dp = nextDp

    return True if val in dp else False


arr = [1, 5, 11, 5]
print(equal_sum_recursive(arr))  # true
print(equal_sum_memo(arr))  # true

arr = [1, 2, 3, 5]
print(equal_sum_recursive(arr))  # false
print(equal_sum_memo(arr))  # false
