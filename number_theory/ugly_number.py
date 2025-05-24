# https://leetcode.com/problems/ugly-number/

def isUgly(n):
    
    if n <= 0:
        return False
    
    for p in [2,3,5]:
        while n % p == 0:
            n = n // p

    return n == 1

# https://leetcode.com/problems/ugly-number-ii/

def nthUglyNumber(n):

    dp = [1]
    i2, i3, i5 = 0, 0, 0

    for _ in range(n):

        next_num = min(dp[i2] * 2, dp[i3] * 3, dp[i5] * 5)
        dp.append(next_num)

        if next_num == dp[i2] * 2:
            i2 += 1
        if next_num == dp[i3] * 3:
            i3 += 1
        if next_num == dp[i5] * 5:
            i5 += 1

    return dp[n - 1]

# https://leetcode.com/problems/ugly-number-iii/

import math

def nthUglyNumber(n, a, b, c):

    def lcm(x, y):
        return x * y // math.gcd(x, y)

    def count(x):
        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(ab, c)
        return (x // a) + (x // b) + (x // c) - (x // ab) - (x // ac) - (x // bc) + (x // abc)

    low, high = 1, 2 * 10**9
    while low < high:
        mid = (low + high) // 2
        if count(mid) < n:
            low = mid + 1
        else:
            high = mid
    return low
