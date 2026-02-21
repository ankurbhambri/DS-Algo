# Brian Kernighan's Algorithm is used to count the number of right most set bits in a number.

# TC: O(k), where k is the number of set bits in the binary representation of the number.

'''

Initial n = 13 (1101), count = 0.

n = n & (n - 1) → 13 & 12 → 1101 & 1100 → 1100 → n = 12, count = 1.

n = n & (n - 1) → 12 & 11 → 1100 & 1011 → 1000 → n = 8, count = 2.

n = n & (n - 1) → 8 & 7 → 1000 & 0111 → 0000 → n = 0, count = 3.

Return count = 3.

'''

def count_set_bits(n):
    count = 0
    while n > 0:
        n = n & (n - 1)   # removes the rightmost set bit
        count += 1
    return count

print(count_set_bits(5))  # 2
print(count_set_bits(6))  # 2
print(count_set_bits(7))  # 3
print(count_set_bits(8))  # 1