# https://leetcode.com/problems/meeting-rooms/

'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106

'''

class Solution:
    def canAttendMeetings(self, intervals):

        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False

        return True


print(Solution().canAttendMeetings([[7,10],[2,4]]))  # Output: True
print(Solution().canAttendMeetings([[0,30],[5,10],[15,20]]))  # Output: False


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

    for _, change in events:
        ongoing += change
        max_rooms = max(max_rooms, ongoing)

    return max_rooms


print(solution([[7, 10], [2, 4]]))
print(solution([[0, 30], [5, 10], [15, 20]]))


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


print(solution2([[7, 10], [2, 4]]))
print(solution2([[0, 30], [5, 10], [15, 20]]))


# similar problem -  https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/


def minGroups(intervals):

    arr = []

    for s, e in intervals:
        arr.append([s, 1])
        arr.append([e + 1, -1])

    arr.sort()

    req = 0
    res = 0

    for _, diff in arr:
        req += diff
        res = max(req, res)

    return res


print(minGroups([[1,3],[5,6],[8,10],[11,13]]))  # Output: 1
print(minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))  # Output: 3