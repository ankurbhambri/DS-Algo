# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/


def maximumSum(nums):

    def func(n):
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s

    hm = {}
    res = -1

    for i in nums:
        val = func(i)

        if val in hm:

            res = max(res, i + hm[val])
            hm[val] = max(i, hm[val])

        else:
            hm[val] = i

    return res


print(maximumSum([51, 71, 17, 42]))  # 93
print(maximumSum([42, 33, 60]))  # 102
print(maximumSum([51, 32, 43]))  # -1
