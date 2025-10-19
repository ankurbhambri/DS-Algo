
# https://leetcode.com/problems/palindromic-substrings/description/

'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

# Similar to longest palindromic substring problem - https://leetcode.com/problems/longest-palindromic-substring/description/

'''

def countSubstrings(s):

    res = 0

    def compare(l, r):

        cnt = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:

            cnt += 1
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


# DP Approach
# TC: O(n^2), SC: O(n^2)
def countSubstrings(s: str) -> int:

    n = len(s)
    count = 0
    dp = [[False] * n for _ in range(n)]

    # Traverse backwards for start index
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            # Check palindrome condition
            if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                dp[i][j] = True
                count += 1

    return count

print(countSubstrings("abc"))
print(countSubstrings("aaa"))


# Variant - Print all palindromic substrings

# TC: O(n^3)
def printSubstrings(s):

    def compare(l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]: # O(n)

            print(s[l:r + 1]) # O(n)
            l -= 1
            r += 1

    for i in range(len(s)): # O(n)

        # odd length palindromes
        compare(i, i)

        # even length palindromes
        compare(i, i + 1)


printSubstrings("abc")
printSubstrings("aaa")


# To reduce it to = TC: O(n^2)
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
