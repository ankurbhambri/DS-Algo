# https://leetcode.com/problems/longest-palindrome/


class Solution:
    def longestPalindrome(self, s: str) -> int:
        character_set = set()
        res = 0

        # Loop over characters in the string
        for c in s:
            # If set contains the character, match found
            if c in character_set:
                character_set.remove(c)
                # Add the two occurrences to our palindrome
                res += 2
            else:
                # Add the character to the set
                character_set.add(c)

        # If any character remains, we have at least one unmatched
        # character to make the center of an odd length palindrome.
        if character_set:
            res += 1

        return res


print(Solution().longestPalindrome("abccccdd"))
print(Solution().longestPalindrome("racecar"))


# Variation of the problem: Largest Palindromic Number

# https://leetcode.com/problems/largest-palindromic-number/
