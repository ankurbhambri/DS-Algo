# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

from collections import Counter

# TC: O(m * n) - We fill a 2D DP table of size m x n.
# SC: O(m * n) - The DP table takes O(m * n) space
class Solution:
    def numWays(self, words: list[str], target: str) -> int:

        n = len(target)

        m = len(words[0])

        mod = 10 ** 9 + 7

        # frequency of each character at every index in "words".
        count = [{} for _ in range(m)]
        for i in range(m):
            for word in words:
                count[i][word[i]] = 1 + count[i].get(word[i], 0)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # only one way to form an empty target string.
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):

            for j in range(1, n + 1):

                # skip
                dp[i][j] = dp[i - 1][j]

                c = count[i - 1].get(target[j - 1], 0)

                # take
                dp[i][j] += (c * dp[i - 1][j - 1]) % mod

        return dp[m][n] % mod


# TC: O(m * n) - We fill a 1D DP table of size n.
# SC: O(n) - The DP table takes O(n) space
class Solution:
    def numWays(self, words: list[str], target: str):

        mod = 10**9 + 7

        n = len(target)

        dp = [1] + [0] * n

        for i in range(len(words[0])):

            count = Counter(w[i] for w in words)

            for j in range(n - 1, -1, -1):
                dp[j + 1] += dp[j] * count.get(target[j], 0) % mod

        return dp[n] % mod


print(Solution().numWays(["abba", "baab"], "bab"))  # 4
print(Solution().numWays(["acca", "bbbb", "caca"], "aba"))  # 6