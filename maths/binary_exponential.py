# calculate binary exponentiation
def binary_exponentiation(base: int, exponent: int) -> int:

    result = 1

    while exponent > 0:
        if exponent % 2 == 1:  # If exponent is odd
            result *= base
        base *= base  # Square the base
        exponent //= 2  # Divide the exponent by 2

    return result


print(binary_exponentiation(2, 10))
