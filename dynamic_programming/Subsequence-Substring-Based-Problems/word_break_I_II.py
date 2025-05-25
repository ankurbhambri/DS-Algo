# https://leetcode.com/problems/word-break/


# Word Break I
def wordBreakI(s, wordDict):

    wordDict = set(wordDict) # Convert to set for O(1) lookups

    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[len(s)]


print(wordBreakI("catsanddog", ["cat", "cats", "and", "sand", "dog"]))

# https://leetcode.com/problems/word-break-ii/


# Word Break II

# Backtracking approach to find all possible sentences
def wordBreakII(s, wordDict):

    wordDict = set(wordDict)
    curr = []
    res = []

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


print(wordBreakII("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
