# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

class Solution:
    def maxValue(self, events, k):
        events.sort()
        n = len(events)
        dp = [[-1] * n for _ in range(k + 1)]
        
        def dfs(cur_index, count, prev_ending_time):
            if cur_index == n or count == k:
                return 0
            if events[cur_index][0] <= prev_ending_time:            
                return dfs(cur_index + 1, count, prev_ending_time)
            
            if dp[count][cur_index] != -1:
                return dp[count][cur_index]
            
            ans = max(dfs(cur_index + 1, count, prev_ending_time), dfs(cur_index + 1, count + 1, events[cur_index][1]) + events[cur_index][2])
            dp[count][cur_index] = ans
            return ans

        return dfs(0, 0, -1)


print(Solution().maxValue([[1,2,4],[3,4,3],[2,3,1]], 2))  # Output: 7
print(Solution().maxValue([[1,2,4],[3,4,3],[2,3,10]], 2))  # Output: 10
print(Solution().maxValue([[1,2,4],[3,4,3],[2,3,10]], 3))  # Output: 13
print(Solution().maxValue([[1,2,4],[3,4,3],[2,3,10]], 1))  # Output: 10
