# https://leetcode.com/problems/sum-of-square-numbers/

# Using HashSet

# Idea behind this approach is that we can find the square of numbers till sqrt(c) and store them in a set.
# Then, we can iterate from 0 to sqrt(c) and check if c - i * i is present in the set or not. If it is present, then we can return True, else we can return False.


def judgeSquareSum(c):
    hs = set()

    n = int(c**0.5)

    for i in range(n + 1):
        hs.add(i * i)

    for j in range(n + 1):
        if j * j <= c:
            num = c - j * j
            if num in hs:
                return True

    return False


# Binary Search similar idea of two sum II

# Idea behind this approach is to use two pointer approach. We can take two pointers l and r, where l = 0 and r = sqrt(c).
# And then we can iterate till l <= r. If l * l + r * r = c, then we can return True, else if l * l + r * r < c, then we can increment l, else we can decrement r.


def judgeSquareSum(c):
    l = 0
    # if we a ^ 2 + b ^ 2 = c in other words a + b = sqrt(c), so that's why we are taking our stopping condition till sqrt(c).
    r = int(c**0.5)

    while l <= r:
        if l * l + r * r == c:
            return True
        elif l * l + r * r < c:
            l += 1
        else:
            r -= 1
    return False
