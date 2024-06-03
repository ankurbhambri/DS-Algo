def validPalindrome(s):

    # helper function to check whether a string is palindrome or not.
    def palindromeCheck(i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    # main logic

    i, j = 0, len(s) - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return palindromeCheck(i + 1, j) or palindromeCheck(i, j - 1)
    return True


print(validPalindrome("abca"))
print(validPalindrome("aba"))
print(validPalindrome("abc"))
