# https://leetcode.com/problems/strange-printer/

# Recursion + Memoization
# TC: O(n^3), SC: O(n^2)
class Solution:
    def strangePrinter(self, s: str) -> int:

        memo = {}

        def solve(i, r):

            # Base Case: Agar string empty hai
            if i > r:
                return 0

            # Agar humne yeh range pehle calculate ki hai
            state = (i, r)
            if state in memo:
                return memo[state]

            # Option 1: s[i] ko alag se print karo, aur baaki solve karo
            res = 1 + solve(i + 1, r)

            # Option 2: s[i] ke jaisa koi aur s[k] dhundo
            for m in range(i + 1, r + 1):
                if s[m] == s[i]:
                    # Humne i aur m ko ek saath print kiya
                    # m index nhi liya kyuki s[i] aur s[m] same hai, toh unko ek saath print kar sakte hai
                    # Isliye range (i, m-1) aur (m+1, r) mein divide kiya
                    res = min(res, solve(i, m - 1) + solve(m + 1, r))

            memo[state] = res
            return res

        return solve(0, len(s) - 1)


# Bottom-up
# Tc: O(n^3) - 3 nested loops, SC: O(n^2) - DP table
class Solution:
    def strangePrinter(self, s: str) -> int:

        n = len(s)

        if n == 0:
            return 0

        # DP Table: dp[i][j] stores min turns for substring s[i...j]
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):

            dp[i][i] = 1 # Single character takes 1 turn

            for j in range(i + 1, n):

                # Default case: print s[i] separately
                dp[i][j] = 1 + dp[i + 1][j]

                # Optimization: if s[k] is same as s[i], try to merge
                for k in range(i + 1, j + 1):

                    if s[i] == s[k]:

                        # dp[i][k-1] handles the first part including the merged char
                        # dp[k+1][j] handles the remaining part
                        res = dp[i][k-1] + (dp[k+1][j] if k+1 <= j else 0)

                        dp[i][j] = min(dp[i][j], res)

        return dp[0][n-1]


print(Solution().strangePrinter("aba"))     # Output: 2
print(Solution().strangePrinter("aaabbb"))  # Output: 2