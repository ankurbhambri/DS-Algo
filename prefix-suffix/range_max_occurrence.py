# https://www.geeksforgeeks.org/queries-to-print-the-character-that-occurs-the-maximum-number-of-times-in-a-given-range/

"""
    Given a string S of size N and Q queries. Every query consists of L and R ( 0 < = L < = R < N ).
    The task is to print the character that occurs the maximum number of times in the given range.
    If there are multiple characters that occur maximum number of times then print the lexicographically smallest of them.

"""


import string


def solution(s, q):
    n = len(s)
    pref = {}
    for ch in string.ascii_lowercase:
        tmp = [0] * (n + 1)
        # first lets mark the positions of the character in the string
        for i in range(n):
            if s[i] == ch:
                # if the character is found at position i, then mark the next position as 1
                # why? because we are going to calculate the prefix sum of the character
                # so if the character is found at position i, then the prefix sum of the character
                # should be increased by 1 at position i + 1 example: [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
                # so the prefix sum of the character 'a' in the string 'abcccabaaabb' is [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
                tmp[i + 1] = 1

        # prefix sum for each character
        for j in range(n):
            tmp[j + 1] += tmp[j]

        pref[ch] = tmp
        # print(pref, ch)

    res = []
    for a, b in q:
        ans = [0, s[a]]
        for ch in string.ascii_lowercase:
            # Now just calculate the frequency of each character in the given range
            freq = pref[ch][b + 1] - pref[ch][a]
            if freq > ans[0]:
                ans = [freq, ch]
        res.append(ans)
    return res


# print(solution("abcccabaaabb", [[2, 4], [1, 8]]))
print(solution("zbacd", [[1, 2], [1, 4]]))
