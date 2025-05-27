# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem


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
