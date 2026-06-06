# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii


class Solution:
    def getWordsInLongestSubsequence(self, words, groups):

        n = len(words)

        def hamming_one(w1, w2):
            if len(w1) != len(w2):
                return False

            diff = 0
            for a, b in zip(w1, w2):
                if a != b:
                    diff += 1
                    if diff > 1:
                        return False

            return diff == 1

        dp = [1] * n
        parent = [-1] * n

        best_len = 1
        best_idx = 0

        for i in range(n):
            for j in range(i):

                if (groups[i] != groups[j] and
                    hamming_one(words[i], words[j])):

                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

            if dp[i] > best_len:
                best_len = dp[i]
                best_idx = i

        ans = []

        cur = best_idx
        while cur != -1:
            ans.append(words[cur])
            cur = parent[cur]

        return ans[::-1]


print(Solution().getWordsInLongestSubsequence(["abc", "abd", "abf", "abg", "abx"], [1, 2, 1, 2, 1]))
print(Solution().getWordsInLongestSubsequence(["abc", "abd", "abf", "abg", "abx"], [1, 1, 1, 1, 1]))