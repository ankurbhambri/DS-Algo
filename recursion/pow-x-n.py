# https://leetcode.com/problems/powx-n/description/

# TC: O(log n)
# SC: O(log n) - recursive stack space
def power(base, exponent):

    if exponent == 0:
        return 1

    half = power(base, exponent // 2)

    res = (half * half)

    # agar exponent odd hai to base ko bhi multiply karna padega
    if exponent % 2 == 1:
        res *= base

    return res


x = 2.00000
n = 10
print(power(x, n))  # Output: 1024.00000

x = 2.00000
n = 3
print(power(x, n))  # Output: 8.00000