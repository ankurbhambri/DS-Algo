# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals):

        res = 0
        intervals.sort()
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:

            if start >= prevEnd:
                prevEnd = end

            else:
                res += 1
                prevEnd = min(prevEnd, end)

        return res


print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # 1
print(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]))      # 2
print(Solution().eraseOverlapIntervals([[1,2],[2,3]]))          # 0
print(Solution().eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))  # 2
