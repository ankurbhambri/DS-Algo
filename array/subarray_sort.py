# Given array of integers find length subarray such that if this subarray is sorted, entire array will be sorted as well.


def solution(arr):

    mn = min(arr)
    mx = max(arr)

    l = 0

    if arr[0] != mn:
        l = 0
    else:
        for i in range(1, len(arr)):
            if arr[i - 1] >= arr[i]:
                l = i - 1
                break

    r = len(arr) - 1
    arr2 = set(arr)

    if arr[-1] < mx:
        r = len(arr)
    else:
        # O(N ^ 2)
        for j in range(len(arr) - 2, -1, -1):  # O(N)
            temp = arr[r]

            if temp - 1 not in arr2:
                temp -= 1
                while temp not in arr:  # O(N)
                    temp -= 1

            if arr[j] != temp:
                r = j
                break

    return r - l + 1, r, l


test = [1, 3, 1, -999, 2, 1, 1, 4, 4]
print(solution(test))

test1 = [2, 6, 4, 8, 10, 9, 15]
print(solution(test1))

test2 = [1, 2, 3, 4, 5, 6, 7]
print(solution(test2)[0], len(test2) - 1)

# print(0 if hello(test2) == len(test2) - 1 else hello(test2))

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
