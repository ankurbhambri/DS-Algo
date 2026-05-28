# https://leetcode.com/problems/longest-happy-prefix/description/

class Solution:
    def longestPrefix(self, s: str) -> str:

        n = len(s)
        lps = [0] * n

        i = 1
        length = 0

        while i < n:

            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1

            else:

                if length != 0:
                    length = lps[length - 1]

                else:
                    lps[i] = 0
                    i += 1

        return s[:lps[-1]]