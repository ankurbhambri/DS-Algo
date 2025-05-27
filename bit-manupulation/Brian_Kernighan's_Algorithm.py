# Brian Kernighan's Algorithm is used to count the number of set bits in a number.


def count_set_bits(n):
    count = 0
    while n:
        rsm = n & -n  # rsm is right most set bit
        n -= rsm
        count += 1
    return count


print(count_set_bits(5))  # 2
print(count_set_bits(6))  # 2
print(count_set_bits(7))  # 3
print(count_set_bits(8))  # 1
