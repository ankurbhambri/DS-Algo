# https://leetcode.com/problems/two-best-non-overlapping-events/

from typing import List
import bisect

# TC: O(N log N)
# SC: O(N)

# Using - Sort + Suffix Maximum Array + Binary Search

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by start time
        events.sort(key=lambda x: x[0])
        n = len(events)

        # Suffix max array: max value from i to end
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], events[i][2])

        # Extract start times for binary search
        starts = [e[0] for e in events]

        ans = 0
        for i in range(n):
            start, end, value = events[i]

            # Find first event with start > current end
            j = bisect.bisect_right(starts, end)

            # Combine current event with best non-overlapping future event
            total = value + suffix_max[j]
            ans = max(ans, total)

        return ans

print(Solution().maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]))  # Output: 4
print(Solution().maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]]))  # Output: 5