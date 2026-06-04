# https://www.spoj.com/problems/GONE/


'''
GONE - G-One Numbers

The War of Evil vs Good continues and Ra-One and G-One continue to be on respective sides.

After saving all the cities with Ra-One Numbers G-One realised that some cities whose population is a "G-One Number" can be easy target for Ra-One.

A G-One number is a number sum of whose digits is a prime number

For example 12 .. sum = 1+2 = 3 ... 3 is a prime number.

G-One wants to find out all the populations which can be g-One numbers....

Can You help him.?

You will be given the range of population and you have to tell him how many in this range are G-One Numbers.

Input
    first line has number 'c' indicating the number of ranges.

    'c' lines follow and contain two numbers ... 'f' and 't' inclusive.

Output
    Print a single line per case giving the number of populations which are G-One numbers.

Example

Input:
    3
    10 19
    1 9
    20 29

Output:
    4
    4
    5
'''

def solve(x):
    
    memo = {}
    s = str(x)

    def isPrime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def dp(pos, tight, cnt):

        if pos == len(s):
            return 1 if isPrime(cnt) else 0

        if (pos, tight, cnt) in memo:
            return memo[(pos, tight, cnt)]

        limit = int(s[pos]) if tight else 9

        ans = 0

        for d in range(limit + 1):
            
            cnt = cnt + d

            new_tight = tight and (d == limit)

            ans += dp(pos + 1, new_tight, cnt)

        memo[(pos, tight, cnt)] = ans
        return ans

    return dp(0, True, 0)


l, r = 10, 19
print(solve(r) - solve(l - 1)) # 4