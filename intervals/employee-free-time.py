# https://leetcode.com/problems/employee-free-time/description/

'''
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.


Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
 

Constraints:

1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8

'''

class Interval:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule):

        intervals = []
        for emp in schedule:
            for interval in emp:
                intervals.append((interval.start, interval.end))

        intervals.sort(key=lambda x: x[0])

        merged = []
        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        free_times = []
        for i in range(1, len(merged)):
            free_times.append(Interval(merged[i-1][1], merged[i][0]))

        return free_times

print(Solution().employeeFreeTime([ [Interval(1,2),Interval(5,6)], [Interval(1,3)], [Interval(4,10)] ]))  # Output: [Interval(3, 4)]
print(Solution().employeeFreeTime([ [Interval(1,3),Interval(6,7)], [Interval(2,4)], [Interval(2,5),Interval(9,12)] ]))  # Output: [Interval(5,6), Interval(7,9)]