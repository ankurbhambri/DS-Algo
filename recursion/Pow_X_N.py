# https://leetcode.com/problems/powx-n/description/

def myPow(x, n):

    if n == 0:
        return 1
    
    if n < 0:
        return myPow(1 / x, -n)

    if n % 2 == 0:
        return myPow(x * x, n // 2)
    
    return x * myPow(x * x, (n - 1) // 2)

x = 2.00000, n = 10
print(myPow(x, n))  # Output: 1024.00000
x = 2.10000, n = 3
print(myPow(x, n))  # Output: 9.26100