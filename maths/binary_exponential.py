# Calculate binary exponentiation
# TC: O(log n)

def binary_exponentiation(base: int, exponent: int) -> int:

    result = 1

    while exponent > 0:

        if exponent % 2 == 1:  # If exponent is odd
            result *= base

        base *= base  # Square the base
        exponent //= 2  # Divide the exponent by 2

    return result


print(binary_exponentiation(2, 10))
print(binary_exponentiation(2, 20))
print(binary_exponentiation(2, 100))


def findPower(base, exponent):

    if exponent == 0:
        return 1

    half = findPower(base, exponent // 2)

    res = half * half

    if exponent % 2 == 1: # if exponent is odd that means we need to multiply the base one more time like 2^3 = (2^2 * 2^1)
        res *= base

    return res

print(findPower(2, 10))
print(findPower(2, 20))
print(findPower(2, 100))
