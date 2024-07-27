"""
Pair Sums

Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are considered different if one pair includes at least one array index which the other doesn't, even if they include the same values.

Signature
int numberOfWays(int[] arr, int k)

Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, 1,000,000,000].
k is in the range [1, 1,000,000,000].

Output
Return the number of different pairs of elements which sum to k.

Example 1
n = 5
k = 6
arr = [1, 2, 3, 4, 3]
output = 2
The valid pairs are 2+4 and 3+3.

Example 2
n = 5
k = 6
arr = [1, 5, 3, 3, 3]
output = 4

There's one valid pair 1+5, and three different valid pairs 3+3 (the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements).

"""

from itertools import combinations


def numberOfWays(nums, k):
    arr = combinations(nums, 2)
    res = 0
    for p in arr:
        if sum(p) == k:
            res += 1
    return res


# another way
def numberOfWays1(nums, k):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    res = 0
    for n in nums:

        diff = k - n

        if diff in freq:
            res += freq[diff]

        # If diff and n are same, that means we've counted the pair (n, n) once extra
        if diff == n:
            res -= 1

    return res // 2


k = 6
arr = [1, 2, 3, 4, 3]
print(numberOfWays(arr, k))
output = 2

k = 6
arr = [1, 5, 3, 3, 3]
print(numberOfWays(arr, k))
# output = 4


k = 6
arr = [1, 2, 3, 4, 3]
print(numberOfWays1(arr, k))
output = 2

k = 6
arr = [1, 5, 3, 3, 3]
print(numberOfWays1(arr, k))
# output = 4
