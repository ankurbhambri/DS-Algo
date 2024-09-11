# https://leetcode.com/problems/meeting-rooms-ii/

"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

"""


def solution(arr):

    arr.sort()

    processes = [0] * (max(arr, key=lambda x: x[1])[1] + 1)

    for s, e in arr:
        processes[s] += 1
        processes[e] = -1

    vm = 0
    res = 0

    for p in processes:
        vm += p
        res = max(res, vm)

    return res


print(solution([[0, 30], [5, 10], [15, 20]]))
print(solution([[7, 10], [2, 4]]))
print(solution([[6, 15], [13, 20], [6, 17]]))


# another approach is two pointer


def solution2(arr):

    start = sorted([s for s, _ in arr])
    end = sorted([e for _, e in arr])

    s, e = 0, 0
    res = 0
    vm = 0
    while s < len(arr):
        if start[s] < end[e]:
            s += 1
            vm += 1
        else:
            e += 1
            vm -= 1

        res = max(res, vm)
    return res


print(solution2([[0, 30], [5, 10], [15, 20]]))
print(solution2([[7, 10], [2, 4]]))
print(solution2([[6, 15], [13, 20], [6, 17]]))
