
# https://leetcode.com/problems/palindromic-substrings/description/

'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

# Similar to longest palindromic substring problem - https://leetcode.com/problems/longest-palindromic-substring/description/

'''

# TC: O(n^2), SC: O(1)
def countSubstrings(s):

    res = 0

    def compare(l, r):

        cnt = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:

            cnt += 1
            print(s[l:r + 1]) # O(n), Variant - To print we can do here, but it will increase the time complexity to O(n^3)
            l -= 1
            r += 1

        return cnt

    for i in range(len(s)):

        # odd length palindromes
        res += compare(i, i)

        # even length palindromes
        res += compare(i, i + 1)

    return res


print(countSubstrings("abc"))
print(countSubstrings("aaa"))


# To reduce it to = TC: O(n^2) for print
# We need to move the print statement out of the while loop, to avoid O(n) substring operation.
def printSubstringsEfficient(s):

    def compare(l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]: # O(n)

            l -= 1
            r += 1

        return l, r

    indices = []
    for i in range(len(s)): # O(n)

        # odd length palindromes
        indices.append(compare(i, i))

        # even length palindromes
        indices.append(compare(i, i + 1))

    for l, r in indices:
        print(s[l + 1:r])  # O(n) but done only for palindromic substrings

    return indices


printSubstringsEfficient("abc")
printSubstringsEfficient("aaa")


# Optmized approach - Manacher's Algorithm - TC: O(n), SC: O(n)
class Solution:
    def countSubstrings(self, s: str) -> int:

        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking

        T = '@#' + '#'.join(s) + '#$'

        n = len(T)

        P = [0] * n

        C = R = 0

        for i in range(1, n - 1):

            if i < R:
                P[i] = min(R - i, P[2 * C - i])  # equals to min(R - i, P[i_mirror])

            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        return sum((v + 1) // 2 for v in P)