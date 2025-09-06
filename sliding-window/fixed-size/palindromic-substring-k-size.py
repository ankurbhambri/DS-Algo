# Given a string and a number k, find the first substring of length k that is a palindrome.

def is_palindrome(s):
    return s == s[::-1]

def find_palindromic_substring(s, k):
    for i in range(len(s) - k + 1):
        if is_palindrome(s[i:i + k]):
            return s[i:i + k]
    return None

print(find_palindromic_substring("abcbadef", 3))  # Output: "bcb"
print(find_palindromic_substring("abaccdbbd", 3))   # Output: "aba"


# instead of slicing, we can use two pointers to check for palindrome

def find_palindromic_substring(s, k):

    n = len(s)

    for i in range(n - k + 1):

        is_pal = True
        left, right = i, i + k - 1

        while left < right:

            if s[left] != s[right]:
                is_pal = False
                break

            left += 1
            right -= 1

        if is_pal:
            return s[i:i + k]

    return None

print(find_palindromic_substring("abcbadef", 3))  # "bcb"
print(find_palindromic_substring("abaccdbbd", 3)) # "aba"
