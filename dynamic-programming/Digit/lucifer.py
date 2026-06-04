# https://www.spoj.com/problems/LUCIFER/

'''
Any number is LUCIFER NUMBER if the difference between sum of digits at even location and sum of digits at odd location is prime number. 

For example, 20314210 is a Lucifer number:

digits at odd location 0, 2, 1, 0.

digits at even location 1, 4, 3, 2.

difference = (1+4+3+2)-(0+2+1+0) = 10-3 = 7 ... a prime number.

Lucifer has access to a warehouse that has lots of weapons. He wants to know in how many ways can he kill him.

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

    def dp(pos, tight, odd_sum, even_sum):

        # odd/even positions right side se count hoti hain, left side se nahi.
        
        if pos == len(s):
            return 1 if isPrime(abs(even_sum - odd_sum)) else 0

        if (pos, tight, odd_sum, even_sum) in memo:
            return memo[(pos, tight, odd_sum, even_sum)]

        limit = int(s[pos]) if tight else 9

        ans = 0

        for d in range(limit + 1):
            
            new_odd_sum = odd_sum + (d if pos % 2 == 0 else 0)
            new_even_sum = even_sum + (d if pos % 2 == 1 else 0)

            new_tight = tight and (d == limit)

            ans += dp(pos + 1, new_tight, new_odd_sum, new_even_sum)

        memo[(pos, tight, odd_sum, even_sum)] = ans
        return ans

    return dp(0, True, 0, 0)