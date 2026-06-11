# https://leetcode.com/problems/longest-palindromic-substring/description/

# Given a string s, return the longest palindromic substring in s.

# Similar to palindromic substrings problem - https://leetcode.com/problems/palindromic-substrings/description/


# TC: O(n^2), SC: O(1)
def longestPalindrome(s):

    def helper(l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l + 1 : r]

    res = ""
    for i in range(len(s)):

        # odd string
        odd = helper(i, i)
        res = odd if len(odd) > len(res) else res

        # even string
        even = helper(i, i + 1)
        res = even if len(even) > len(res) else res

    return res


print(longestPalindrome("babad"))
print(longestPalindrome("racecar"))


# TC: O(N), SC: O(n) - Manacher's Algorithm
class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Step 1: String ko modify karna (e.g., "aba" -> "#a#b#a#")
        T = "#" + "#".join(s) + "#"

        n = len(T)

        P = [0] * n  # Palindrome radius store karne ke liye

        C = 0        # Center
        R = 0        # Right Boundary

        max_len = 0      # Sabse bade palindrome ki length
        center_index = 0 # Us bade palindrome ka center

        # Step 2: Har index par loop chalana
        for i in range(n):

            i_mirror = 2 * C - i

            # Agar 'i' boundary ke andar hai, toh mirror ka data copy karo
            if i < R:
                P[i] = min(R - i, P[i_mirror])

            # Boundary ke bahar characters ko manually check karke expand karo
            while (i - 1 - P[i]) >= 0 and (i + 1 + P[i]) < n and T[i - 1 - P[i]] == T[i + 1 + P[i]]:
                P[i] += 1

            # Agar naya palindrome right boundary 'R' ke bahar nikal gaya, toh C aur R ko update karo
            if i + P[i] > R:
                C = i
                R = i + P[i]

            # Sabse max length track karna
            if P[i] > max_len:
                max_len = P[i]
                center_index = i

        # Step 3: Original string mein se answer nikalna
        start = (center_index - max_len) // 2

        return s[start : start + max_len]
