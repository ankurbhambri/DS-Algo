# https://leetcode.com/problems/paint-house/

# similar, ninja training problem, but here we have 3 colors and we want to minimize the cost instead of maximizing the points.
# similar to vacation problem (atcoder), but here we have 3 colors and we want to minimize the cost instead of maximizing the points.

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

            # here, idea is to add the current cost to the minimum of the previous house for the other two colors.

            # if i am select first option then what is the minimum cost of painting the previous house with the other two colors, and so on for the other two options.

            dp0 = min(dp[1], dp[2]) + costs[i][0]

            dp1 = min(dp[0], dp[2]) + costs[i][1]

            dp2 = min(dp[0], dp[1]) + costs[i][2]

            dp = [dp0, dp1, dp2]

        return min(dp)


print(Solution().minCost([[7,6,2]])) # 2
print(Solution().minCost([[17,2,17],[16,16,5],[14,3,19]])) # 10


# https://leetcode.com/problems/paint-house-ii/

# TC: O(n * k) where n is the number of houses and k is the number of colors
# SC: O(1) space complexity
class Solution:
    def minCostII(self, costs):

        n, k = len(costs), len(costs[0])

        prev = costs[0]

        for i in range(1, n):

            curr = costs[i]

            min1 = min(prev)

            min1_idx = prev.index(min1)

            min2 = min(prev[:min1_idx] + prev[min1_idx + 1:])

            for j in range(k):
                curr[j] += min1 if j != min1_idx else min2

            prev = curr

        return min(prev)


print(Solution().minCostII([[1,5],[2,9]])) # 3
print(Solution().minCostII([[1,3],[2,4]])) # 5