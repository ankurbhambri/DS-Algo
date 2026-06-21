# Very powerful technique to solve many problems such as: (hard to meduim level)

# https://leetcode.com/problems/2-keys-keyboard/
# https://leetcode.com/problems/prime-arrangements/
# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
# https://leetcode.com/problems/prime-palindrome/


# n // 2 humme quotient deta h, Tells us how many times 2 perfectly fits into n.Example: 11 // 2 = `5`
# n % 2 humme remainder deta h, Tells us what is left after dividing n by 2. Example: 11 % 2 = `1`

# TC: O(sqrt(n)) - because we are checking for factors only up to the square root of n.
# SC: O(log(n)) - because the number of prime factors of n is at most log(n).
def prime_factorization(n):

        d = 2
        factors = []

        while d * d <= n:

            while n % d == 0:

                factors.append(d)

                n //= d

            d += 1

        if n > 1:
            factors.append(n)

        return factors


print(prime_factorization(18))  # Output: [2, 3, 3], because 18 can be factored into 2 * 3 * 3
print(prime_factorization(28))  # Output: [2, 2, 7], because 28 can be factored into 2 * 2 * 7


# Prime number kaise check karein code.
# TC: O(sqrt(n)) - because we are checking for factors only up to the square root of n.
# SC: O(1) - because we are using a constant amount of space.
def is_prime(num):
     
    if num < 2:
        return False

    d = 2
    while d * d <= num:
        if num % d == 0:
            return False
        d += 1

    return True


# Factorial kaise nikalte hain code.
# TC: O(n) - because we are multiplying n numbers together.
# SC: O(1) - because we are using a constant amount of space.
def factorial(x):
    ans = 1

    for i in range(2, x + 1):
        ans *= i

    return ans