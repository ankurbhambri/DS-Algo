# https://leetcode.com/problems/word-break/


# Word Break I
def wordBreakI(s, wordDict):

    w = set(wordDict)

    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in w:
                dp[i] = True
                break

    return dp[len(s)]


print(wordBreakI("catsanddog", ["cat", "cats", "and", "sand", "dog"]))


# Word Break II
def wordBreakII(s, wordDict):

    w = set(wordDict)

    def helper(i):

        if i == len(s):
            return res.append(" ".join(curr))

        for j in range(i, len(s)):
            a = s[i : j + 1]
            if a in w:
                curr.append(a)
                helper(j + 1)
                curr.pop()

    curr = []
    res = []
    helper(0)
    return res


print(wordBreakII("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
