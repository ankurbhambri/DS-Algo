# https://leetcode.com/problems/paint-house/

'''
    We are given an array costs where costs[i][0] is the cost of painting house i with color red,

    costs[i][1] is the cost of painting house i with color blue, and costs[i][2] is the cost of painting house i with color green.
'''

# TC: O(n) where n is the number of houses
# Space optimal solution, O(1) space complexity
class Solution:
    def minCost(self, costs):

        dp = [0, 0, 0]

        for i in range(len(costs)):

            dp0 = min(dp[1], dp[2]) + costs[i][0]
            dp1 = min(dp[0], dp[2]) + costs[i][1]
            dp2 = min(dp[1], dp[0]) + costs[i][2]
            dp = [dp0, dp1, dp2]

        return min(dp)


print(Solution().minCost([[7,6,2]])) # 2
print(Solution().minCost([[17,2,17],[16,16,5],[14,3,19]])) # 10