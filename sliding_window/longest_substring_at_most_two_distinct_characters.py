'''
Given a string, find the length of the longest substring S that contains at most 2 distinct characters.
'''

from collections import defaultdict

class Solution:
    def length_of_longest_substring_two_distinct(self, s: str) -> int:

        l = 0
        res = 0
        freq = dict()

        for r in range(len(s)):
            w = s[r]
            
            # calculating frequency here of all characters
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1
 
            while len(freq) > 2:
                wl = s[l]

                freq[wl] -= 1

                l += 1

                if freq[wl] == 0:

                    del freq[wl]

            res = max(res, r - l + 1)

        return res
