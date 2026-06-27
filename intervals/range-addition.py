# https://leetcode.com/problems/range-addition/description/


def rangeAddition(n, updates):

    res = [0] * n

    # formula - add the value at start and subtract the value at end + 1
    for start, end, inc in updates:
        res[start] += inc
        if end + 1 < n:
            res[end + 1] -= inc

    # cummulative sum in the end
    for i in range(1, n):
        res[i] += res[i - 1]

    return res


print(rangeAddition(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]))  # Output: [-2, 0, 3, 5, 3]
print(
    rangeAddition(10, [[2, 4, 6], [5, 6, 8], [1, 9, -4]])
)  # Output: [0, 6, 2, 2, 2, 10, 8, 8, 8, 8]
print(
    rangeAddition(10, [[2, 4, 6], [5, 6, 8], [1, 9, -4], [0, 9, 5]])
)  # Output: [5, 11, 7, 7, 7, 15, 13, 13, 13, 13]
