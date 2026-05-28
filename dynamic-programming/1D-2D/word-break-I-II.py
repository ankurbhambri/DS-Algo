from typing import List

# Word Break I
# https://leetcode.com/problems/word-break/


def wordBreakI(s, wordDict):

    wordDict = set(wordDict) # Convert to set for O(1) lookups

    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j : i] in wordDict:
                dp[i] = True
                break

    return dp[len(s)]


print(wordBreakI("catsanddog", ["cat", "cats", "and", "sand", "dog"])) # True


# Word Break II
# https://leetcode.com/problems/word-break-ii/


# Backtracking approach to find all possible sentences
def wordBreakII(s, wordDict):

    res = []
    curr = []
    wordDict = set(wordDict)

    def helper(i):

        if i == len(s):
            return res.append(" ".join(curr))

        for j in range(i, len(s)):

            a = s[i : j + 1]

            if a in wordDict:

                curr.append(a)

                helper(j + 1)

                curr.pop()

    helper(0)
    return res


print(wordBreakII("catsanddog", ["cat", "cats", "and", "sand", "dog"])) # ["cat sand dog", "cats and dog"]
print(wordBreakII("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])) # ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]

# Memoisation
class Solution:
    def wordBreakII(self, s: str, wordDict: List[str]) -> List[str]:

        memo = {}
        wordSet = set(wordDict)

        def dfs(i):

            if i in memo:
                return memo[i]

            if i == len(s):
                return [""]   # base case

            res = []

            for j in range(i + 1, len(s) + 1):

                word = s[i : j]

                if word in wordSet:

                    sub_sentences = dfs(j)

                    for sub in sub_sentences:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)

            memo[i] = res
            return res

        return dfs(0)

print(Solution().wordBreakII("catsanddog", ["cat", "cats", "and", "sand", "dog"])) # ["cat sand dog", "cats and dog"]
print(Solution().wordBreakII("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])) # ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]