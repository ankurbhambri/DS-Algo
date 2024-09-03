# Very powerful technique to solve many problems such as: (hard to meduim level)
# https://leetcode.com/problems/2-keys-keyboard/
# https://leetcode.com/problems/prime-arrangements/
# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
# https://leetcode.com/problems/prime-palindrome/


def prime_factorization(n):

    factors = 0  # or []
    d = 2
    while n >= 2:
        if n % d == 0:
            factors += d  # factors.append(d)
            n = n // d
        else:
            d += 1
    return factors


print(prime_factorization(18))  # 2 * 3 * 3 = 18
print(prime_factorization(315))  # 3 * 3 * 5 * 7 = 315
print(prime_factorization(100))  # 2 * 2 * 5 * 5 = 100
print(prime_factorization(17))  # 17
print(prime_factorization(13))  # 13
print(prime_factorization(1))  # 0
print(prime_factorization(0))  # 0
