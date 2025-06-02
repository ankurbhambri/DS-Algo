# https://leetcode.com/problems/concatenated-words/

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):

        d = set(words)
        memo = {}

        def dfs(word):
            for i in range(1, len(word)):

                prefix = word[:i]
                suffix = word[i:]

                if word in memo:
                    return memo[word]

                if (
                    (prefix in d and suffix in d) or
                    (prefix in d and dfs(suffix)) or
                    (suffix in d and dfs(prefix))
                ):
                    memo[word] = True
                    return memo[word]
            
            memo[word] = False
            return memo[word]
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)

        return res

print(Solution().findAllConcatenatedWordsInADict(["cat", "cats", "dog", "catsdog", "catdog", "dogcat"]))  # ['catsdog', 'catdog', 'dogcat']
print(Solution().findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))  # ["catsdogcats","dogcatsdog","ratcatdogcat"]