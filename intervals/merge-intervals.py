# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals):

        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):

            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])

            else:
                res.append(intervals[i])

        return res

print(Solution().merge([[1, 3],[2, 6],[8,10],[15, 18]]))
print(Solution().merge([[1, 3],[4, 6],[0, 3],[15, 18]])) # Will fail for these type of cases, but will work fine at leetcode


# Line sweep approach
class Solution:
    def merge_intervals(self, intervals):

        events = []
        for start, end in intervals: 
            events.append((start, True))  # Start event
            events.append((end, False))   # End event

        events.sort()
        
        result = []
        active = 0
        curr_start = None
        

        for time, is_start in events:
            if is_start:

                if active == 0:
                    curr_start = time
                active += 1
            else:
            
                active -= 1
                if active == 0:
                    result.append([curr_start, time])
        
        return result

print(Solution().merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge_intervals([[1,3],[4,6],[0,3],[15,18]]))

# Variant

'''

Given two array intervals A and B where intervals in A have no overlap in A and intervals in B have no overlap in B.
Furthermore, A[i], B[i] = [starti, endi], merge all overlapping intervals between the two interval lists,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Note: Both A and B are sorted by start in ascending order.

Example 1:
Input:
    A = [[3,11], [14,15], [18,22], [23,24], [25,26]],
    B = [[2,8], [13,20]]

Output: [[2,11], [13,22], [23,24], [25,26]]

Example 2:
Input: A = [], B = [[0,4], [10,13]]
Output: [[0,4], [10,13]]

Constraints:
• 0 < A. length, B. length <= 104
• A[i]-length == B[i].length == 2
• 0 < starti<= endi <= 104

'''

class Solution:
    def mergeTwoIntervalLists(self, A, B):

        res = []
        i, j = 0, 0

        def merger_intervals(interval):
            if res and res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)

        while i < len(A) and j < len(B):

            if A[i][0] <= B[j][0]:
                merger_intervals(A[i])
                i += 1

            else:
                merger_intervals(B[j])
                j += 1

        while i < len(A):
            merger_intervals(A[i])
            i += 1

        while j < len(B):
            merger_intervals(B[j])
            j += 1

        return res

print(Solution().mergeTwoIntervalLists([], [[0,4], [10,13]])) # Output: [[0,4], [10,13]]
print(Solution().mergeTwoIntervalLists([[3,11], [14,15], [18,22], [23,24], [25,26]], [[2,8], [13,20]])) # Output: [[2,11], [13,22], [23,24], [25,26]]