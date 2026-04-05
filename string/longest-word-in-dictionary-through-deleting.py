# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

# TC: O(N * M) where N is number of words in dictionary and M is length of longest word
# SC: O(1) if we don't consider output space, else O(N * M) in worst case when all words are longest and valid

class Solution:
    def findLongestWord(self, s, dictionary):

        dictionary.sort(key=lambda w: (-len(w), w))

        def is_subsequence(word):
            i = j = 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            return j == len(word)

        for word in dictionary:
            if is_subsequence(word):
                return word

        return ""

print(Solution().findLongestWord("abpcplea", ["a","b","c"]))  # Output: "a"
print(Solution().findLongestWord("abpcplea", ["ale","apple","monkey","plea"]))  # Output: "apple"