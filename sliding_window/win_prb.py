# https://www.hackerrank.com/challenges/sherlock-and-anagrams?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


def sherlockAndAnagrams(s):
    res = 0
    # win = 1
    # n = len(s) - 1
    # while n > 0:
    #     d = {}
    #     for i in range(0, len(s)):
    #         if i < len(s) - 1:
    #             sub = "".join(sorted(s[i: i + win]))
    #             d[sub] = 1 + d.get(sub, 0)
    #             res += d[sub]
    #     win += 1
    #     n -= 1
    # return res
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
