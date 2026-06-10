# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/


# TC: O(n^3)
# SC: O(n^2)
class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:

        n = len(arr)

        dp = [[0] * n for _ in range(n)]

        max_val = [[0] * n for _ in range(n)]

        for i in range(n):
            max_val[i][i] = arr[i]
            for j in range(i, n):
                max_val[i][j] = max(max_val[i][j - 1], arr[j])

        for length in range(2, n + 1):

            for i in range(n - length + 1):

                j = i + length - 1

                dp[i][j] = float('inf')

                for k in range(i, j):

                    cost = dp[i][k] + dp[k+1][j] + (max_val[i][k] * max_val[k+1][j])

                    dp[i][j] = min(dp[i][j], cost)

        return dp[0][n-1]


# OPTIMAL SOLUTION
# Monotonic Stack

# TC: O(n)
# SC: O(n)
class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:

        cost = 0
        stack = []

        for num in arr:

            while stack and stack[-1] <= num:

                # ye mid element hai jo stack se nikal raha hai
                mid = stack.pop()

                # mid ke left mein stack ka top element hoga (agar stack empty nahi hai
                left = stack[-1] if stack else float('inf')

                # and right mein current `num` hoga
                cost += mid * min(left, num)

            stack.append(num)

        while len(stack) > 1:
            cost += stack.pop() * stack[-1]

        return cost


print(Solution().mctFromLeafValues([4, 11]))  # Output: 44
print(Solution().mctFromLeafValues([6, 2, 4]))  # Output: 32