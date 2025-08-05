# https://leetcode.com/problems/longest-repeating-character-replacement


# Question: Given a string s and an integer k, return the length of the longest substring that can be obtained by replacing at most k characters in s.
# The substring must consist of the same character after replacements.


# TC: O(26 * n) -> O(n)
# SC: O(26) -> O(1)


# Here, the idea is will keep on expending the windows, util our condition is not met.

# The condition is: if the difference between the length of the window and the most frequent character in the window is less than or equal to k, we keep expanding; otherwise, we start reducing from the left.

# Length of the window - max frequency of character in the window <= k -> expand the window else reduce from left.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        res = 0
        freq = {}

        for r in range(len(s)):

            freq[s[r]] = 1 + freq.get(s[r], 0)

            max_val = max(freq.values())

            while (r - l + 1) - max_val > k:

                freq[s[l]] -= 1

                l += 1

            res = max(res, r - l + 1)

        return res


print(Solution().characterReplacement("ABAB", 2))  # Output: 4
print(Solution().characterReplacement("AABABBA", 1))  # Output: 4
print(Solution().characterReplacement("AABABBA", 2))  # Output: 5
print(Solution().characterReplacement("AABABBA", 0))  # Output: 2
