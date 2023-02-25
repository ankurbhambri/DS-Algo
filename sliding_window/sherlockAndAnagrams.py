# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

def sherlockAndAnagrams(s):
    res = 0
    for i in range(1, len(s)):
        d = {}
        for j in range(0, len(s) - i + 1):  # till length of s - i + 1
            # sliding window
            sub = "".join(sorted(s[j : j + i]))  # sorted return list
            d[sub] = 1 + d.get(sub, 0)
            res += (
                d[sub] - 1
            )  # if there is only one anagram then it's not good
    return res
