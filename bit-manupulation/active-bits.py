# Check if a particular bit is set (active)

def is_bit_set(n, k):
    return (n & (1 << k)) != 0

# Check LSB (rightmost bit) is set or not

def is_lsb_set(n):
    return (n & 1) == 1

# Remove LSB (right shift by 1)
def remove_lsb(n):
    return n >> 1

# Brian Kernighan’s Algorithm

# Removes the rightmost set bit each time.

def count_set_bits(n):
    count = 0
    while n > 0:
        n = n & (n - 1)   # removes rightmost 1 bit
        count += 1
    return count

# Bit-by-bit check (Basic)

def count_set_bits(n):
    count = 0
    while n > 0:
        count += n & 1   # check LSB
        n >>= 1         # right shift
    return count