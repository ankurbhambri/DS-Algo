def longestPalindrome(s):

    def helper(l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l + 1 : r]

    res = ""
    for i in range(len(s)):

        # odd string
        test = helper(i, i)
        res = test if len(test) > len(res) else res

        # even string
        test = helper(i, i + 1)
        res = test if len(test) > len(res) else res

    return res


print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("racecar"))


# In case simple Palindromic Substrings are asked, we can use the below code snippet:


def countSubstrings(s):
    res = 0

    def compare(l, r):

        res = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:

            res += 1
            l -= 1
            r += 1

        return res

    for i in range(len(s)):

        res += compare(i, i)

        res += compare(i, i + 1)

    return res


print(countSubstrings("abc"))
print(countSubstrings("aaa"))
