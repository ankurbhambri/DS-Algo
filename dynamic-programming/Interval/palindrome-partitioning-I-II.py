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
                print(start, end)
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

            if ispal(s[i : j + 1]): # like a, aaa and aba cases
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
        if n <= 1:
            return 0

        # Palindrome table (Yeh aapka bilkul sahi tha)
        isPal = [[False] * n for _ in range(n)]

        for i in range(n):
            isPal[i][i] = True

        for length in range(2, n + 1):

            for i in range(n - length + 1):

                j = i + length - 1

                if s[i] == s[j]:

                    if length == 2 or isPal[i + 1][j - 1]:

                        isPal[i][j] = True


        # dp[i] ko unke max possible cuts (jo ki khud index 'i' hai) se fill karenge
        # Example: 0th index ke liye max 0 cuts, 1st index ke liye max 1 cut, etc.
        dp = [i for i in range(n)] 

        for i in range(n):

            for j in range(i + 1):

                if isPal[j][i]:
                    # Agar poori string j=0 se lekar i tak palindrome hai, toh 0 cuts chahiye
                    if j == 0:
                        dp[i] = 0
                    else:
                        # Agar j > 0 hai, toh humne ek naya j - 1 aur j ke beech mein lagaya taaki j se i wala palindrome alag ho sake.
                        dp[i] = min(dp[i], dp[j - 1] + 1)
        
        return dp[-1]


print(Solution().minCut("aab"))  # 1
print(Solution().minCut("a"))  # 0
print(Solution().minCut("ab"))  # 1
print(Solution().minCut("racecar"))  # 0