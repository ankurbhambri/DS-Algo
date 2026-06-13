# https://leetcode.com/problems/longest-string-chain/


class Solution:
    def longestStrChain(self, words):

        dp = {}
        ans = 1
        words.sort(key=len)

        for word in words:

            dp[word] = 1

            for i in range(len(word)):

                prev = word[:i] + word[i+1:]

                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)

            ans = max(ans, dp[word])

        return ans


print(Solution().longestStrChain(["a","b","ba","bca","bda","bdca"])) # 4
print(Solution().longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"])) # 5