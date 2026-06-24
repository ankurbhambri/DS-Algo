# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # String 's' ko words ki list mein convert karo space ke basis par
        words = s.split()

        # Agar dono ki length alag hai, toh pattern kabhi match nahi ho sakta
        if len(pattern) != len(words):
            return False

        char_to_word = {}  # Letter se Word ki mapping ke liye
        visited_words = set() # Jo words hum use kar chuke hain unhe track karne ke liye

        # Ek-ek karke pattern ka letter aur s ka word uthao
        for letter, word in zip(pattern, words):

            # Case 1: Agar yeh letter pehle aa chuka hai
            if letter in char_to_word:

                # Check karo ki kya yeh usi word se map ho raha hai ya nhi
                if char_to_word[letter] != word:
                    return False

            # Case 2: Agar letter naya hai
            else:
                # Lekin woh word pehle hi kisi aur letter ko map hua h, toh pattern match nahi hoga
                if word in visited_words:
                    return False

                # Agar sab sahi hai, toh naye letter aur word ko map kar do
                char_to_word[letter] = word
                visited_words.add(word)

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