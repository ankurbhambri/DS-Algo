# https://www.geeksforgeeks.org/minimum-length-unsorted-subarray-sorting-which-makes-the-complete-array-sorted/
# https://www.youtube.com/watch?v=TGWkLukqnls

# Given array of integers find length subarray such that if this subarray is sorted, entire array will be sorted as well.


def solution(arr):

    mn = float("-inf")
    mx = float("inf")

    l = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            l = i
            break

    r = len(arr) - 1

    for j in range(len(arr) - 2, -1, -1):
        if arr[j] > arr[j + 1]:
            r = j
            break

    if l == 0 and r == len(arr) - 1:
        return 0

    mn = min(arr[l : r + 1])
    mx = max(arr[l : r + 1])

    for i in range(0, l + 1):
        if arr[i] > mn:
            l = i
            break

    for j in range(len(arr) - 1, -r, -1):
        print(j, arr[j])
        if arr[j] < mx:
            r = j
            break

    return r - l + 1, r, l


test = [1, 3, 1, -999, 2, 1, 1, 4, 4]
print(solution(test))

test1 = [2, 6, 4, 8, 10, 9, 15]
print(solution(test1))

test2 = [1, 2, 3, 4, 5, 6, 7]
print(solution(test2))

test3 = [1, 2, 4, -1, 0, 3, 5, 7]
print(solution(test3))

test4 = [1, 2, 2, 2, 1, 2, 3]
print(solution(test4))

#    i            i

# 1 1 1 1 2 3 4 4
# NLogN


# 1 3 1 -999 2 1 1 4 4

# 0 1 2 3    4 5 6 7 8
# j


# arr = set(arr)
# mn
# mx

# arr[0] < -999

# l = 0

# 4 - 1 or 4 in set:


# mn = -999
# mx = 4

# l = 1 O(N) - 3
# r = 5 O(N) - 1

# O(2N)


# O(NLogN)


# res = max(j - 1, res)
# w = 2, 3, [4] + [1]#
