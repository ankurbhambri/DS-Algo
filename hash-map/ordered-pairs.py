'''
You are given an array arr. Count the number of ordered pairs (i, j) such that:

a[i] - a[j] = i - j      where 0 ≤ i, j < n
Important notes:

(i, j) and (j, i) are counted as different.
(i, i) is also a valid pair.
Examples:

Input:  [2, 4, 6, 5, 9, 9, 11]
Output: 13

Input:  [1, 2, 3]
Output: 9
Explanation for [1, 2, 3]:

For index 0 → 3 valid pairs
For index 1 → 3 valid pairs
For index 2 → 3 valid pairs
Total = 9

'''


from collections import Counter

def countPairs(arr):
    freq = Counter()

    for i, x in enumerate(arr):
        freq[x - i] += 1

    ans = 0

    for f in freq.values():
        ans += f * f

    return ans