# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        hm = {}
        nsl = s.split(' ')

        if len(nsl) != len(pattern):
            return False
        
        for i in range(len(nsl)):

            key = pattern[i]
            val = nsl[i]

            if key not in hm:
                if val in hm.values():
                    return False
                hm[key] = val

            else:
                if val != hm[key]:
                    return False  

        return True


print(Solution().wordPattern("abba", "dog cat cat dog")) # True
print(Solution().wordPattern("abba", "dog cat cat fish")) # False


# https://leetcode.com/problems/word-pattern-ii/

'''
Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to non-empty strings,
such that if each character in pattern is replaced by the string it maps to, then the resulting string is s.
A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.


Example 1:

Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
Example 2:

Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"
Example 3:

Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false
'''

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        char_to_word = {}
        used_words = set()

        def backtrack(i, j):
            # both consumed
            if i == len(pattern) and j == len(s):
                return True

            # one consumed, other not
            if i == len(pattern) or j == len(s):
                return False

            ch = pattern[i]

            # already mapped
            if ch in char_to_word:
                word = char_to_word[ch]

                # substring must match
                if not s.startswith(word, j):
                    return False

                return backtrack(i + 1, j + len(word))

            # try every possible substring
            for k in range(j, len(s)):

                word = s[j:k + 1]

                # bijection check
                if word in used_words:
                    continue

                char_to_word[ch] = word
                used_words.add(word)

                if backtrack(i + 1, k + 1):
                    return True

                # backtrack
                del char_to_word[ch]
                used_words.remove(word)

            return False

        return backtrack(0, 0)


print(Solution().wordPatternMatch("aaaa", "asdasdasdasd")) # True
print(Solution().wordPatternMatch("abab", "redblueredblue")) # True