'''
Given an array of integers. We are required to write a program 
to print the number of factors of every element of the given array.
'''


def func(arr):
    res = {}
    res = []
    for n in arr:
        c = 0
        i = 1
        while i <= n:
            if n % i == 0:
                c += 1
            i += 1
        res.append(c)
    return res


print(func([10, 12, 14]))


def NosFactor(n):
    if n in [0, 1, 2]:
        return 1
    if n == 3:
        return 2
    else:
        return NosFactor(n - 1) + NosFactor(n - 3) + NosFactor(n - 4)


print(NosFactor(5))

# Top down approach
def NosFactor_DP(n):
    dp = {0: 1, 1: 1, 2: 1, 3: 2}
    if n not in dp:
        dp[n] = NosFactor_DP(n - 1) + NosFactor_DP(n - 3) + NosFactor_DP(n - 4)
    return dp[n]


print(NosFactor_DP(5))


# Bottom up approach
def NosFactor_TB(n):
    tb = [1, 1, 1, 2]
    for i in range(4, n + 1):
        tb.append(tb[i - 1] + tb[i - 3] + tb[i - 4])
    return tb[n]


print(NosFactor_TB(5))
