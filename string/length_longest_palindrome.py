# https://leetcode.com/problems/longest-palindrome/


def longestPalindrome(s):

    frequency_map = {}

    for c in s:
        frequency_map[c] = frequency_map.get(c, 0) + 1

    res = 0
    has_odd_frequency = False
    for freq in frequency_map.values():
        # Check if the frequency is even, add the whole frquency to the result
        if (freq % 2) == 0:
            res += freq
        else:
            # If the frequency is odd, one occurrence of the character will remain without a match
            res += freq - 1
            has_odd_frequency = True

    # If has_odd_frequency is true, we have at least one unmatched, character to make the center of an odd length palindrome.
    if has_odd_frequency:
        return res + 1

    return res


print(longestPalindrome("abccccdd"))
print(longestPalindrome("racecar"))
