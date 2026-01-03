# https://leetcode.com/problems/employee-free-time/description/

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