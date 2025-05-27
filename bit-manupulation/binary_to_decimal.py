def binary_to_decimal(binary_str):
    decimal = 0
    power = len(binary_str) - 1
    for digit in binary_str:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

print(int("101010", 2))

print(binary_to_decimal("101010"))
print(binary_to_decimal("1000"))
print(binary_to_decimal('100'))
print(binary_to_decimal("1100"))

