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
