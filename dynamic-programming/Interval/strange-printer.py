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

            state = (i, r)

            if state in memo:
                return memo[state]

            # Option 1: s[i] ko alag se print karo, aur baaki solve karo
            res = 1 + solve(i + 1, r)

            # Option 2: s[i] ke jaisa koi aur s[k] dhundo
            for m in range(i + 1, r + 1):
                if s[m] == s[i]:
                    # Humne i aur m ko ek saath print kiya, ek lambi line banayi, jaha same element s[m] == s[i] use print kar diya
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

        # DP Table: dp[i][j] batayega s[i...j] ko print karne ka min cost
        dp = [[0] * n for _ in range(n)]

        # Step 1: Base Case (Length = 1)
        # Kisi bhi single character ko print karne mein 1 hi turn lagta hai
        for i in range(n):
            dp[i][i] = 1 # Single character takes 1 turn

        # Step 2: Baki saari lengths ke liye loop chalayein (Length 2 se lekar n tak)
        for length in range(2, n + 1):

            for i in range(n - length + 1):

                j = i + length - 1

                # Worst case scenario: Pehle character ko alag se print karein
                # aur baki bache [i+1...j] ko alag se.
                dp[i][j] = 1 + dp[i + 1][j] # Default case: print s[i] separately

                # Smart Option: Ab beech mein check karein koi s[i] ke jaisa character hai kya
                for k in range(i + 1, j + 1):

                    # Agar s[k] == s[i] hai, toh s[k] ko print karne ka kharcha free!
                    if s[i] == s[k]:

                        # Isliye hum subproblems ko [i...k-1] aur [k+1...j] mein tod dete hain.
                        res = dp[i][k - 1] + (dp[k + 1][j] if k + 1 <= j else 0)

                        # Minimum turns ko update karein
                        dp[i][j] = min(dp[i][j], res)

        return dp[0][n-1]


print(Solution().strangePrinter("aba"))     # Output: 2
print(Solution().strangePrinter("aaabbb"))  # Output: 2