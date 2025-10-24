'''
For an array of positive integers arr[n] and an integer k,
a subarray is good if it contains at least k distinct integers.

You must find the minimum length of such a good subarray.
If no such subarray exists, return -1.

Input:
arr = [2, 2, 1, 1, 3]
k = 3

Output:
4
'''

def findMinimumLengthSubarray(arr,k):
    freq = {}
    l, d = 0, 0
    res = float('inf')
    for r in range(len(arr)):
        freq[arr[r]] = freq.get(arr[r], 0) + 1
        if freq[arr[r]] == 1:
            d += 1
            while d >= k:
                res = min(res, r - l + 1)
                freq[arr[l]] -= 1
                if freq[arr[l]] == 0:
                    d -= 1
                l += 1
    return res

print(findMinimumLengthSubarray([2, 2, 1, 1, 3], 3))
