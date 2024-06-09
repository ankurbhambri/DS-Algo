"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res


"""
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

Given a string, find the length of the longest substring S that contains at most 2 distinct characters.

"""


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


"""
    https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

    Given a string S, find the length of the longest substring T that contains at most k distinct characters.

    Note - same as above replace static value 2 with k only

"""


class Solution:

    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        l = 0
        res = 0
        freq = dict()

        for r in range(len(s)):
            w = s[r]
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1
            while len(freq) > k:
                wl = s[l]

                freq[wl] -= 1

                l += 1

                if freq[wl] == 0:

                    del freq[wl]

            res = max(res, r - l + 1)

        return res
