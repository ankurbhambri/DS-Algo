# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

# Question: Given a string s, find the number of unordered pairs of substrings of s that are anagrams of each other.
# An anagram is a word or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.
# For example, the anagrams of 'abc' are 'abc', 'acb', 'bac', 'bca', 'cab', and 'cba'.

# The function should return the number of unordered pairs of substrings that are anagrams of each other.


def sherlockAndAnagrams(s):

    freq_dict = {}
    res = 0

    for i in range(len(s)):
        for j in range(i, len(s)):

            # Get the substring
            substr = s[i : j + 1]

            # Sort the substring to get its character combination
            sorted_substr = "".join(sorted(substr))

            freq_dict[sorted_substr] = 1 + freq_dict.get(sorted_substr, 0)

            # if there is only one anagram then it's not good
            res += freq_dict[sorted_substr] - 1

    return res

print(sherlockAndAnagrams("abba"))  # Output: 4
print(sherlockAndAnagrams("abcd"))  # Output: 0
