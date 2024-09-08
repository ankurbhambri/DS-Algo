"""

Merge 3 sorted arrays, removing duplicates from the result. The constraint is to deal with all 3 arrays in a single pass and without extra memory (other than the final result array)

5 mins: Questions to the interviewer

"""


def merger_arrays(a, b, c):

    res = []
    i, j, k = 0, 0, 0

    while i < len(a) or j < len(b) or k < len(c):

        a_val = a[i] if i < len(a) else float("inf")
        b_val = b[j] if j < len(b) else float("inf")
        c_val = c[k] if k < len(c) else float("inf")

        min_val = min(a_val, min(b_val, c_val))

        res.append(min_val)

        while i < len(a) and a[i] == min_val:
            i += 1

        while j < len(b) and b[j] == min_val:
            j += 1

        while k < len(c) and c[k] == min_val:
            k += 1

    return res


# TC - O(N + M + K) for 3 arrays
# Sc - O(N) for string the result


arr1 = [1, 2, 3, 4, 5]
arr2 = [0, 4, 5, 6, 7]
arr3 = [3, 5, 7, 8, 9]

print(merger_arrays(arr1, arr2, arr3))


arr1 = [1, 2, 3, 3, 3, 3]
arr2 = [2, 4, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8]
arr3 = [0, 0, 0, 0, 3, 5, 7, 7, 8, 8, 9, 9, 9, 9, 9, 9, 10, 11, 11]

print(merger_arrays(arr1, arr2, arr3))
