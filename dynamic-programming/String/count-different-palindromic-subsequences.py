# https://leetcode.com/problems/count-different-palindromic-subsequences/

# TC: O(N^3) due to the three nested loops, SC: O(N^2) due to the dp table.
# SC: O(N^2)
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:

        MOD = 10**9 + 7
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):

                j = i + length - 1

                # kitne palindromes 'a' se start/end hote hain?
                # kitne 'b' se?
                # kitne 'c' se?
                # kitne 'd' se?
                for c in 'abcd':
                    # find leftmost occurrence of c in s[i..j]
                    lo = -1
                    for k in range(i, j + 1):
                        if s[k] == c:
                            lo = k
                            break

                    # find rightmost occurrence of c in s[i..j]
                    hi = -1
                    for k in range(j, i - 1, -1):
                        if s[k] == c:
                            hi = k
                            break

                    if lo == -1: # a is not present in s[i..j], ignore
                        pass
                    elif lo == hi: # a is present only once in s[i..j], count it as a palindrome
                        dp[i][j] += 1
                    elif hi == lo + 1: # a is present twice in s[i..j], count "a" and "aa" as palindromes
                        dp[i][j] += 2
                    else: # a is present more than twice in s[i..j], count "a", "aa", and all palindromes in s[lo+1..hi-1] surrounded by "a"
                        dp[i][j] += 2 + dp[lo + 1][hi - 1]

                dp[i][j] %= MOD

        return dp[0][n - 1]