# https://leetcode.com/problems/meeting-rooms-ii/

"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

"""

# Line Sweep approach

def solution(intervals):

    events = []

    for start, end in intervals:
        events.append((start, 1))   # meeting starts
        events.append((end, -1))    # meeting ends

    # Sort events: by time, then by type (-1 before +1 if times are equal)
    events.sort()

    max_rooms = 0
    ongoing = 0

    for time, change in events:
        ongoing += change
        max_rooms = max(max_rooms, ongoing)

    return max_rooms


print(solution([[0, 30], [5, 10], [15, 20]]))
print(solution([[7, 10], [2, 4]]))
print(solution([[6, 15], [13, 20], [6, 17]]))


# Another approach is two pointer

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


# similar problem -  https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/


def minGroups(intervals):

    arr = []

    for s, e in intervals:
        arr.append([s, 1])
        arr.append([e + 1, -1])

    arr.sort()

    req = 0
    res = 0

    for a, diff in arr:
        req += diff
        res = max(req, res)

    return res


print(minGroups([[1,3],[5,6],[8,10],[11,13]]))  # Output: 1
print(minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))  # Output: 3
