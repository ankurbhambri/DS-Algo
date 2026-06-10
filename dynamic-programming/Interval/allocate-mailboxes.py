# https://leetcode.com/problems/allocate-mailboxes/


# TC: O(n^2 * k)
# SC: O(n^2 + n * k)

# recusion + memoization
class Solution:
    def minDistance(self, houses, k):

        houses.sort()
        n = len(houses)

        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, n):

                m = (i + j) // 2

                for t in range(i, j + 1):
                    cost[i][j] += abs(houses[t] - houses[m])

        memo = {}

        def dfs(i, k):

            if i == n and k == 0:
                return 0

            if (i, k) in memo:
                return memo[(i, k)]

            ans = float('inf')

            for j in range(i, n):

                ans = min(ans, cost[i][j] + dfs(j + 1, k - 1))

            memo[(i, k)] = ans
            return ans

        return dfs(0, k)


print(Solution().minDistance([1, 4, 8, 10, 20], 3)) # 5
print(Solution().minDistance([2, 3, 5, 12, 18], 2)) # 9