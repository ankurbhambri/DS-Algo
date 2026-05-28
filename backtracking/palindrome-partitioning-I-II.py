 # https://leetcode.com/problems/palindrome-partitioning/

# Question: Given a string s, partition s such that every substring of the partition is a palindrome.

# Tc: O(n * 2^n)
# SC:  O(n) (stack) + O(2^n * n) (output)
class Solution:
    def partition(self, s):

        res = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):

            if start == len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if is_palindrome(sub): # condition to check if substring is palindrome
                    path.append(sub)
                    backtrack(end, path)
                    path.pop() # backtrack to explore other partitions

        backtrack(0, [])
        return res


print(Solution().partition("aab"))  # [['a', 'a', 'b'], ['aa', 'b']]
print(Solution().partition("a"))  # [['a']]
print(Solution().partition("racecar"))  # [['r', 'a', 'c', 'e', 'c', 'a', 'r'], ['r', 'a', 'c', 'e', 'c', 'a', 'r']]
print(Solution().partition("ab"))  # [['a', 'b']]


# https://leetcode.com/problems/palindrome-partitioning-ii


# TC: O(n^3) and SC: O(n^2)
class Solution:
    def minCut(self, s):

        memo = [[-1] * len(s) for _ in range(len(s))]

        def ispal(s):
            return s == s[::-1]

        def solve(i, j):

            if i >= j:
                return 0

            if ispal(s[i : j + 1]): # like a and aaa cases
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            min_step = float("inf")
            for k in range(i, j):
                if ispal(s[i : k + 1]):
                    cut = 1 + solve(k + 1, j)
                    min_step = min(min_step, cut)

            memo[i][j] = min_step
            return memo[i][j]

        return solve(0, len(s) - 1)


# Bottom-up approach

# TC: O(n^2) and SC: O(n^2)
class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)

        # palindrome table
        isPal = [[False] * n for _ in range(n)]

        # every single char palindrome
        for i in range(n):
            isPal[i][i] = True

        # fill table
        for length in range(2, n + 1):
            for i in range(n - length + 1):

                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2 or isPal[i + 1][j - 1]:
                        isPal[i][j] = True

        dp = [0] * n

        for i in range(n - 1, -1, -1):

            # worst case
            dp[i] = float('inf')

            for j in range(i, n):

                if isPal[i][j]:

                    # whole remaining string palindrome
                    if j == n - 1:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], 1 + dp[j + 1])

        return dp[0]


print(Solution().minCut("aab"))  # 1
print(Solution().minCut("a"))  # 0
print(Solution().minCut("ab"))  # 1
print(Solution().minCut("racecar"))  # 0