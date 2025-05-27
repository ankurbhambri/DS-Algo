# Example number
num = 42  # Binary: 101010

# Set the bit at position 'n' (e.g., position 3)
n = 3
mask = 1 << n  # Shift 1 by 'n' positions to create the mask

# Use bitwise OR to set the bit at position n
num |= mask

print(f"Number with bit {n} set: {num}")
