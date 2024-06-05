# https://leetcode.com/problems/largest-palindromic-number/

from collections import Counter


def largestPalindromic(num):

    count = Counter(num)
    palindrome = mid = ""

    for d in sorted(count.keys(), reverse=True):
        # odd values should go in the middle, checking wih bitwise operator
        mid = max(mid, d * (count[d] & 1))
        # even values should go on the sides and taking their half values so that in the last we can reverse the string and add it to the palindrome
        palindrome += d * (count[d] // 2)

    # removing any leading zeros
    palindrome = palindrome.lstrip("0")
    return (palindrome + mid + palindrome[::-1]) or "0"


print(largestPalindromic("444947137"))
