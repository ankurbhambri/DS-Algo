# https://leetcode.com/problems/russian-doll-envelopes/

# similar question - https://leetcode.com/problems/maximum-height-by-stacking-cuboids/


# TC: O(n^2)
# SC: O(n)

# TLE
from bisect import bisect


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:

        if not envelopes:
            return 0

        # Step 1: Sort the envelopes normally
        envelopes.sort()
        
        n = len(envelopes)

        # dp[i] stores the max envelopes chain ending with envelopes[i]
        dp = [1] * n 
        
        # Step 2: Standard LIS-style DP
        for i in range(n):
            for j in range(i):
                # Check if envelope j fits strictly inside envelope i
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp)


# Optmised approach using binary search

class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:

        # Sort width ascending, height descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Find LIS on heights
        tails = []
        for _, h in envelopes:
            idx = bisect.bisect_left(tails, h)
            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h

        return len(tails)