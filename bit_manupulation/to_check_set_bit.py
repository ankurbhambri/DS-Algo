def is_bit_set(number, n):
    # Shift 1 to the left by (n - 1) positions to create a mask for the nth bit
    mask = 1 << (n - 1)
    # Perform bitwise AND to check if the nth bit is set
    return (number & mask) != 0


number = 0b000010000000000000000000
print(is_bit_set(number, 20))
