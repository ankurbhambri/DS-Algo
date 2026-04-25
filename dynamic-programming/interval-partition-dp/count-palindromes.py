# https://algo.monster/problems/dp_interval_intro

# Given a string, count how many of its substrings are palindromes. A single character counts as a palindrome.


# TC: O(N^2), SC: O(N^2) due to dp table. Can be optimized to O(N) using Manacher's algorithm, but let's stick to DP for clarity.
def count_palindromes(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    # Base case: single characters (length 1)
    count = 0
    for i in range(n):
        dp[i][i] = True
        count += 1

    for length in range(2, n + 1):        # substring length: 2, 3, ..., n
        for l in range(n - length + 1):   # l + length - 1 must be < n
            r = l + length - 1            # right endpoint
            if s[l] == s[r] and (length == 2 or dp[l + 1][r - 1]):
                dp[l][r] = True
                count += 1

    return count

print(count_palindromes("abac"))  # Output: 5 (a, b, a, c, aba)
print(count_palindromes("aaa"))  # Output: 6 (a, a, a, aa, aa, aaa)


# Manacher's Algorithm (O(N) time, O(N) space)
def count_palindromes_manacher(s):
    # Transform the string to handle even-length palindromes
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n  # p[i] will hold the radius of the palindrome centered at i
    center = right = 0
    count = 0

    for i in range(n):
        mirror = 2 * center - i  # mirror index of i around center

        if i < right:
            p[i] = min(right - i, p[mirror])

        # Expand around center i
        while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        # Update center and right boundary if the palindrome expanded past right
        if i + p[i] > right:
            center, right = i, i + p[i]

        # Each palindrome contributes (p[i] + 1) // 2 palindromic substrings in the original string
        count += (p[i] + 1) // 2

    return count