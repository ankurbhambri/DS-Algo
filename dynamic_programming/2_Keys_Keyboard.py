# https://leetcode.com/problems/2-keys-keyboard/

# Backtracking solution


def minSteps(n):

    if n == 1:
        return 0

    memo = {}

    def helper(curr_len, paste_len):

        if curr_len == n:
            return 0
        if curr_len > n:
            return 10000

        if (curr_len, paste_len) in memo:
            memo[(curr_len, paste_len)]

        opt1 = 1 + helper(curr_len + paste_len, paste_len)

        opt2 = 2 + helper(curr_len + curr_len, curr_len)

        memo[(curr_len, paste_len)] = min(opt1, opt2)

        return memo[(curr_len, paste_len)]

    return 1 + helper(1, 1)


print(minSteps(3))  # 3
print(minSteps(1))  # 0
print(minSteps(6))  # 5
print(minSteps(18))  # 8
print(minSteps(315))  # 17


# We can solve this problem using prime factorization technique more optimimum way.


def minSteps_primeFactors(n):

    factors = 0
    divisor = 2

    while n >= 2:
        if n % divisor == 0:
            factors += divisor
            n //= divisor
        else:
            divisor += 1

    return factors


print(minSteps_primeFactors(3))  # 3
print(minSteps_primeFactors(1))  # 0
print(minSteps_primeFactors(6))  # 5
print(minSteps_primeFactors(18))  # 8
print(minSteps_primeFactors(315))  # 17
