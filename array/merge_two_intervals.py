"""
Given A and B two interval lists, A has no overlap inside A and B has no overlap inside B. Write the function to merge two interval lists, output the result with no overlap. Ask for a very efficient solution

A naive method can combine the two list, and sort and apply merge interval in the leetcode, but is not efficient enough.

For example,
A: [1,5], [10,14], [16,18]
B: [2,6], [8,10], [11,20]

output [1,6], [8, 20]

"""


def solution(A, B):

    i = 0
    j = 0
    res = []

    while i < len(A) or j < len(B):

        if i == len(A):
            curr = B[j]
            j += 1
        elif j == len(B):
            curr = A[i]
            i += 1
        elif A[i][0] < B[j][0]:
            curr = A[i]
            i += 1
        else:
            curr = B[j]
            j += 1

        if res and res[-1][1] >= curr[0]:
            res[-1][1] = max(res[-1][1], curr[1])
        else:
            res.append(curr)

    return res


A = [[1, 5], [10, 14], [16, 18]]
B = [[2, 6], [8, 10], [11, 20]]

print(solution(A, B))  # [[1,6], [8, 20]]

A = [[1, 5]]
B = [[6, 10]]

print(solution(A, B))  # [[1, 5], [6, 10]]

A = [[1, 3], [5, 7], [9, 11]]
B = [[1, 3], [5, 7], [9, 11]]

print(solution(A, B))  # [[1, 3], [5, 7], [9, 11]]


# Another approach


# TC: O(N * M), SC: O(1)
def merge(arr1, l1, arr2, l2):
    for i in range(l1):
        # compare the current element from arr1 with the first element of the second array
        if arr1[i] > arr2[0]:
            # swap if the element in the first array is greater than the element in the second array
            arr1[i], arr2[0] = arr2[0], arr1[i]
        # sort second array in non-decreasing order
        first = arr2[0]
        pos = 1
        while pos < l2 and arr2[pos] < first:
            arr2[pos - 1] = arr2[pos]
            pos += 1
        arr2[pos - 1] = first
        i += 1


n = 4
nums1 = [2, 9, 11, 15]

m = 6
nums2 = [-18, 1, 3, 7, 10, 12]
print(merge(nums1, n, nums2, m))

# Two sorted arrays and merge them.


# TC: O(n + m), SC: O(N)


import math


def next_gap(gap):
    if gap <= 1:
        return 0
    return math.ceil(gap / 2)


def merge(array1, array2):
    n = len(array1)
    m = len(array2)

    # Initial gap
    gap = next_gap(n + m)

    while gap > 0:
        # Comparing elements in the first array
        i = 0
        while i + gap < n:
            if array1[i] > array1[i + gap]:
                array1[i], array1[i + gap] = array1[i + gap], array1[i]
            i += 1

        # Comparing elements between the first and second array
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if array1[i] > array2[j]:
                array1[i], array2[j] = array2[j], array1[i]
            i += 1
            j += 1

        # Comparing elements in the second array
        if j < m:
            while j + gap < m:
                if array2[j] > array2[j + gap]:
                    array2[j], array2[j + gap] = array2[j + gap], array2[j]
                j += 1

        # Reduce the gap for the next iteration
        gap = next_gap(gap)

    return array1 + array2


# Example usage
array1 = [1, 5, 10, 14]
array2 = [2, 6, 8, 11]

print(merge(array1, array2))
print("Array 1:", array1)  # [1, 2, 3, 5]
print("Array 2:", array2)  # [8, 9, 10, 13, 14]

# TC: O(n log m), SC: O(1)
